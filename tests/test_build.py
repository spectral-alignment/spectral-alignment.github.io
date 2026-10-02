from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from bs4 import BeautifulSoup
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import build


class MarkdownPublishingTests(unittest.TestCase):
    def render(self, source):
        with tempfile.TemporaryDirectory() as directory:
            content = Path(directory) / 'content.md'
            output = Path(directory) / 'index.html'
            content.write_text(source)
            with redirect_stdout(io.StringIO()):
                build(content, output)
            return output.read_text()

    def test_editorial_changes_reach_every_part_of_the_page(self):
        source = (ROOT / 'content.md').read_text()
        header, body = source[4:].split('\n---\n', 1)
        config = yaml.safe_load(header)
        config['title'] = 'Updated title\nUpdated second line'
        config['description'] = 'An updated search description.'
        config['authors'][0]['name'] = 'Updated author'
        config['links']['code']['label'] = 'Source code'
        config['contents'][0]['label'] = 'Start here'
        config['metrics'][0]['after'] = '69%'
        config['figures']['pipeline']['alt'] = 'Updated figure description.'
        config['explorer']['wide'] = 'Updated slider explanation.'
        config['ui']['expanded_figure'] = 'Image preview'
        body = body.replace('## What should a world model preserve?', '## Updated introduction')
        body = body.replace('A world model needs enough information', 'An updated world model needs enough information')
        body = body.replace('**Figure 1. Planning success.**', '**Updated planning caption.**')
        body = body.replace('| Scene average | 0.84 | **0.93** |', '| Scene average | 0.84 | **0.94** |')
        body = body.replace(r'K_{ij}=\exp', r'J_{ij}=\exp')
        rendered = self.render('---\n' + yaml.safe_dump(config, allow_unicode=True, sort_keys=False) + '---\n' + body)
        page = BeautifulSoup(rendered, 'html.parser')
        self.assertEqual(page.title.string, 'Updated title Updated second line')
        self.assertEqual(page.select_one('.hero h1').get_text(' '), 'Updated title Updated second line')
        self.assertEqual(page.select_one('meta[name=description]')['content'], config['description'])
        self.assertIn('Updated author', page.select_one('.authors').get_text())
        self.assertTrue(all(a.get_text().endswith('Source code') for a in page.select('a[href="https://anonymous.4open.science/r/SpecWM/"]')))
        self.assertEqual(page.select_one('.toc a').string, 'Start here')
        self.assertEqual(page.select_one('.metric strong').string, '69%')
        self.assertEqual(page.select_one('img[src="assets/pipeline.png"]')['alt'], 'Updated figure description.')
        self.assertEqual(page.select_one('#overview h2').string, 'Updated introduction')
        self.assertTrue(page.select_one('.lead').get_text().startswith('An updated world model'))
        self.assertIn('Updated planning caption.', page.select_one('img[src="assets/fair_cem.png"]').find_parent('figure').figcaption.get_text())
        self.assertEqual(page.select_one('#representations tbody strong').string, '0.94')
        self.assertTrue(page.select_one('.equation .math-tex').string.startswith(r'J_{ij}=\exp'))
        self.assertEqual(page.select_one('#figure-dialog')['aria-label'], 'Image preview')
        interactive = json.loads(page.select_one('#site-text').string)
        self.assertEqual(interactive['explorer']['wide'], 'Updated slider explanation.')

    def test_nested_figures_and_theorems_keep_their_layout(self):
        page = BeautifulSoup(self.render((ROOT / 'content.md').read_text()), 'html.parser')
        self.assertEqual(len(page.select('article > section')), 8)
        self.assertEqual(len(page.select('figure')), 10)
        self.assertEqual(len(page.select('.ablation')), 3)
        self.assertEqual(len(page.select('.paired > figure')), 2)
        self.assertEqual(len(page.select('#theory > .theory-result')), 5)
        self.assertEqual(len(page.select('.steps > .step')), 3)
        self.assertEqual(len(page.select('table')), 2)
        self.assertEqual(len(page.select('#equal-author-names > span')), 2)
        self.assertIn(r'\begin{aligned}', page.select_one('#successor-measure .equation .math-tex').string)
        self.assertNotIn('SPECTRALMATHTOKEN', str(page))
        self.assertNotIn(':::', page.get_text())

    def test_unclosed_layout_marker_fails_the_build(self):
        with self.assertRaisesRegex(ValueError, 'Unclosed Markdown directive'):
            self.render((ROOT / 'content.md').read_text() + '\n:::note\nUnclosed note\n')

    def test_generated_html_is_reproducible(self):
        source = (ROOT / 'content.md').read_text()
        self.assertEqual(self.render(source), self.render(source))


if __name__ == '__main__':
    unittest.main()
