"""Build the static page from content.md; no content is fetched at runtime."""
from pathlib import Path
import argparse
import html
import json
import math
import re

from bs4 import BeautifulSoup
import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]


def escape(value):
    return html.escape(str(value), quote=True)


def inner(element):
    return ''.join(str(child) for child in element.contents)


def text_template(template, **values):
    for key, value in values.items():
        template = template.replace('{' + key + '}', str(value))
    return template


def math_span(tex, display=False):
    span = '<span class="math-tex"' + (' data-display="true"' if display else '') + '>' + escape(tex) + '</span>'
    return '<div class="equation">' + span + '</div>' if display else span


def resource(config, name, button=False, icon=False):
    link = config['links'][name]
    external = ' target="_blank" rel="noopener"' if link['url'].startswith('https://') else ''
    css = ' class="button"' if button else ''
    symbol = '<span aria-hidden="true">〈/〉</span>' if icon else ''
    return f'<a{css} href="{escape(link["url"])}"{external}>{symbol}{escape(link["label"])}</a>'


def explorer(config):
    labels = config['explorer']
    description = text_template(labels['description'], similarity=f'{math.exp(-1):.2f}', band=labels['medium'])
    aria = text_template(labels['aria'], sigma=7, similarity=f'{math.exp(-1):.2f}')
    return f'''<div class="explorer">
<div class="explorer-header"><h3>{escape(labels['title'])}</h3><span class="tag">{escape(labels['tag'])}</span></div>
<div class="explorer-layout"><div><canvas id="kernel-canvas" width="460" height="460" role="img" aria-label="{escape(aria)}"></canvas>
<div class="legend"><span>{escape(labels['low'])}</span><i></i><span>{escape(labels['high'])}</span></div></div>
<div><label for="bandwidth">{escape(labels['label'])} <output id="sigma-value" for="bandwidth">7</output></label>
<input id="bandwidth" type="range" min="1" max="20" value="7" step="1">
<div class="formula">{math_span(labels['formula'])}</div>
<p id="kernel-description" aria-live="polite">{escape(description)}</p><p>{escape(labels['hint'])}</p></div></div></div>'''


def render_body(body, config):
    equations = {}

    def store_math(match):
        key = f'SPECTRALMATHTOKEN{len(equations):04d}END'
        display = match.group(1) is not None
        equations[key] = math_span(match.group(1) if display else match.group(2), display)
        return '\n\n' + key + '\n\n' if display else key

    body = re.sub(r'\$\$\s*\n(.*?)\n\s*\$\$|\$([^\n$]+)\$', store_math, body, flags=re.S)
    lines, stack = [], []
    for line in body.splitlines():
        if line.strip() == ':::':
            if not stack:
                raise ValueError('Unexpected directive closing line')
            lines.append('</' + stack.pop() + '>\n')
            continue
        match = re.fullmatch(r':::([\w-]+)(?: (.*))?', line)
        if not match:
            lines.append(line)
            continue
        kind, args = match.group(1), (match.group(2) or '')
        if kind == 'details':
            state, label = args.split('|', 1)
            opened = ' open' if state.strip() == 'open' else ''
            lines.append(f'<details class="ablation"{opened} markdown="1"><summary>{escape(label.strip())}</summary>\n')
            stack.append('details')
        elif kind == 'theorem':
            identifier, label = args.split('|', 1)
            lines.append(f'<div class="theory-result" id="{escape(identifier.strip())}" markdown="1"><p class="result-label">{escape(label.strip())}</p>\n')
            stack.append('div')
        elif kind in ('figure', 'table'):
            lines.append(f'<div data-{kind}="{escape(args)}" markdown="1">\n')
            stack.append('div')
        elif kind in ('note', 'lead', 'table-caption', 'steps', 'paired'):
            lines.append(f'<div class="{kind}" markdown="1">\n')
            stack.append('div')
        elif kind == 'explorer':
            lines.append('<div data-explorer="true" markdown="1">\n')
            stack.append('div')
        elif kind == 'actions':
            if args not in config['links']:
                raise ValueError('Unknown resource: ' + args)
            lines.append(f'<div class="actions" style="justify-content:flex-start">{resource(config, args, button=True)}\n')
            stack.append('div')
        else:
            raise ValueError('Unknown directive: ' + kind)
    if stack:
        raise ValueError('Unclosed Markdown directive')
    rendered = markdown.markdown('\n'.join(lines), extensions=['extra', 'sane_lists'])
    for key, equation in equations.items():
        rendered = rendered.replace('<p>' + key + '</p>', equation).replace(key, equation)
    soup = BeautifulSoup(rendered, 'html.parser')

    for element in soup.select('div.lead, div.table-caption'):
        paragraph = element.find('p', recursive=False)
        if paragraph is None:
            raise ValueError('A lead or table-caption directive needs a paragraph')
        paragraph['class'] = element['class']
        element.unwrap()
    for element in soup.select('div.note'):
        element.name = 'aside'
        for paragraph in element.find_all('p', recursive=False):
            paragraph.unwrap()
    for element in soup.select('p.result-label'):
        element.name = 'span'
    for element in soup.select('[data-explorer]'):
        element.replace_with(BeautifulSoup(explorer(config), 'html.parser'))
    for element in soup.select('[data-figure]'):
        figure = config['figures'][element['data-figure']]
        loading = f' loading="{escape(figure["loading"])}"' if 'loading' in figure else ''
        caption = inner(element)
        caption_soup = BeautifulSoup(caption, 'html.parser')
        for paragraph in caption_soup.find_all('p', recursive=False):
            paragraph.unwrap()
        label = caption_soup.find('strong')
        if label:
            label.name = 'span'
            label['class'] = 'figure-label'
        element.replace_with(BeautifulSoup(f'''<figure><a class="figure-link" href="{escape(figure['fallback'])}" data-zoom="{escape(figure['zoom'])}" data-title="{escape(figure['title'])}"><img src="{escape(figure['image'])}" width="{figure['width']}" height="{figure['height']}"{loading} alt="{escape(figure['alt'])}"></a><figcaption>{caption_soup}</figcaption></figure>''', 'html.parser'))
    for element in soup.select('[data-table]'):
        table_config = config['tables'][element['data-table']]
        del element['data-table']
        element['class'] = 'table-wrap'
        table = element.table
        if table is None:
            raise ValueError('A table directive needs a Markdown table')
        if table_config.get('caption'):
            caption = soup.new_tag('caption', attrs={'class': 'sr-only', 'style': 'text-align:left;padding:10px 12px;font-size:12px;color:#626b76'})
            caption.string = table_config['caption']
            table.insert(0, caption)
        for row in table.select('tr'):
            cells = row.find_all(['td', 'th'], recursive=False)
            for cell in cells:
                cell.attrs.pop('style', None)
                if cell.name == 'th':
                    cell['scope'] = 'col'
            cells[table_config['highlight']]['class'] = 'highlight'
    for element in soup.select('.steps'):
        steps = BeautifulSoup('', 'html.parser')
        step = None
        for child in list(element.children):
            if getattr(child, 'name', None) == 'h3':
                step = steps.new_tag('div', attrs={'class': 'step'})
                steps.append(step)
                child.name = 'b'
                step.append(child.extract())
            elif getattr(child, 'name', None) == 'p':
                if step is None:
                    raise ValueError('Each step needs a ### heading')
                child.name = 'span'
                step.append(child.extract())
        element.clear()
        element.append(steps)

    output = BeautifulSoup('', 'html.parser')
    teaser = BeautifulSoup('', 'html.parser')
    section = None
    entries = {entry['id']: (index, entry) for index, entry in enumerate(config['contents'], 1)}
    found = []
    for child in list(soup.children):
        if getattr(child, 'name', None) == 'h2':
            identifier = child.attrs.pop('id', None)
            if identifier not in entries:
                raise ValueError('A ## heading needs an ID listed in contents: ' + str(identifier))
            index, entry = entries[identifier]
            found.append(identifier)
            section = output.new_tag('section', id=identifier)
            output.append(section)
            label = output.new_tag('span', attrs={'class': 'section-num'})
            label.string = f'{index:02d} / {entry["section_label"]}'
            section.append(label)
        (section if section is not None else teaser).append(child.extract())
    if found != [entry['id'] for entry in config['contents']]:
        raise ValueError('Section order must match contents')
    for figure in teaser.find_all('figure'):
        figure['class'] = 'teaser abstract-figure'
    return str(teaser), str(output)


def build(content_path, output_path):
    source = content_path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n(.*)\Z', source, re.S)
    if not match:
        raise ValueError('content.md must start with YAML front matter')
    config, body = yaml.safe_load(match.group(1)), match.group(2)
    teaser, article = render_body(body, config)
    author_html = lambda author: f'<span>{escape(author["name"])}<sup>{escape(author["affiliation"])}</sup></span>'
    equal = ''.join(author_html(a) for a in config['authors'] if a.get('equal'))
    other = ''.join(author_html(a) for a in config['authors'] if not a.get('equal'))
    authors = (f'<span class="equal-authors">{{<span id="equal-author-names">{equal}</span>}}</span>' if equal else '') + other
    affiliations = ''.join(f'<span><sup>{escape(a["marker"])}</sup> {escape(a["name"])}</span>' for a in config['affiliations'])
    title_lines = config['title'].splitlines()
    hero_title = '<br>'.join(escape(line) for line in title_lines)
    hero = f'''<div class="hero"><h1>{hero_title}</h1><p class="subtitle">{escape(config['subtitle'])}</p><div class="byline"><div class="authors">{authors}</div><div class="affiliations">{affiliations}</div><div class="author-note">{escape(config['author_note'])}</div></div><div class="actions">{resource(config, 'code', button=True, icon=True)}</div></div>'''
    navigation = ''.join(resource(config, item['link']) if 'link' in item else f'<a href="{escape(item["url"])}">{escape(item["label"])}</a>' for item in config['navigation'])
    contents = ''.join(f'<a href="#{escape(item["id"])}">{escape(item["label"])}</a>' for item in config['contents'])
    metrics = ''.join(f'<div class="metric"><div class="value"><span>{escape(m["before"])}</span><strong>{escape(m["after"])}</strong></div><p>{escape(m["label"])}</p><small>{escape(m["change"])}</small></div>' for m in config['metrics'])
    interactive_text = json.dumps({'explorer': config['explorer'], 'figure_close_hint': config['ui']['figure_close_hint']}, ensure_ascii=False).replace('<', '\\u003c')
    values = dict({key: escape(value) for key, value in config['ui'].items()}, title=escape(' '.join(title_lines)), description=escape(config['description']), hero=hero,
                  navigation=navigation, contents_links=contents, metrics=metrics, teaser=teaser, article=article,
                  interactive_text=interactive_text)
    template = (ROOT / 'site/template.html').read_text()
    result = re.sub(r'\{\{(\w+)\}\}', lambda m: values[m.group(1)], template)
    document = BeautifulSoup(result, 'html.parser')
    identifiers = [tag['id'] for tag in document.select('[id]')]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Duplicate HTML IDs')
    for anchor in document.select('a[href^="#"]'):
        if anchor['href'][1:] not in identifiers:
            raise ValueError('Broken section link: ' + anchor['href'])
    for image in document.select('img[src], [data-zoom]'):
        asset = image.get('src') or image['data-zoom']
        if not (ROOT / 'dist' / asset.split('?', 1)[0]).is_file():
            raise ValueError('Missing image asset: ' + asset)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result)
    print(f'Built {output_path.relative_to(ROOT) if output_path.is_relative_to(ROOT) else output_path} from {content_path.name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--content', type=Path, default=ROOT / 'content.md')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist/index.html')
    args = parser.parse_args()
    build(args.content, args.output)
