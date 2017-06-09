
OK, the whitepaper is complicated to build.  I'm sorry but that's the way it is.

- We want Google Docs for collaborative editing, commenting, and contribution by people who aren't familiar with Git.
- We want Markdown so we'll be able to copy-paste it into steemit.com, and so we can use LaTeX via Pandoc.
- We want the document to be version controlled so we can use Git to see history, do experiments in branches, etc.
- Images are created in Inkscape with SVG, but Google Docs doesn't allow SVG uploads (except via very convoluted workarounds).
- Actually Pandoc doesn't allow with PDF output either due to limitations in LaTeX [reference](https://github.com/jgm/pandoc/issues/265).

Google Docs has limitations though:

- No plaintext.
- No Markdown.
- If you just enter a Markdown document and convert it to text by copy-pasting, it loses formatting (in particular dashes for list items are turned into some sort of non-selectable entity)
- I tried looking up how to use Google API's to download the document as a file, but it looked really complicated and I gave up after 20 minutes trying to figure out how to use it and not making progress.

It Would Be Nice if the Google Doc was the "main" version and the Markdown version was updated from it.  But because Google Docs is such a crappy product, that's simply not possible.

