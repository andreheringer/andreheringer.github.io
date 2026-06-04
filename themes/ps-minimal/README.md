# ps-minimal

A minimal Pelican theme inspired by the [PlanetScale](https://planetscale.com/blog) blog.

## Design tokens

| Token | Value | Use |
| --- | --- | --- |
| `--bg` | `#fafafa` | Page background |
| `--text` | `#1a1a1a` | Primary text |
| `--muted` | `#818181` | Secondary text (meta lines, nav) |
| `--rule` | `#e1e1e1` | Borders and separators |
| `--accent` | `#15f365` | Links on hover, active state, category tab |
| `--code-bg` | `#f4f4f4` | Code block background |

## Fonts

- **Inter** (400/500/600) — body text and headings, loaded from Google Fonts
- **Cascadia Code** (400/500/600) — code blocks, loaded from Google Fonts

## Layout

- Article body max-width: 720px
- Index/listings max-width: 960px
- Sticky site header with brand on the left and a horizontal nav on the right
- Simple one-line site footer

## Files

- `static/css/style.css` — all styles
- `templates/base.html` — page shell
- `templates/index.html` — blog index (paginated)
- `templates/article.html` — single post
- `templates/page.html` — static page
- `templates/article_list.html` — paginated category/tag/author listing
- `templates/_partials/post_card.html` — single post entry in a list
- `templates/_partials/category_tabs.html` — `All | <category>…` tab row
- `templates/_partials/pagination.html` — page navigation
- `templates/_partials/header.html` / `footer.html` — site chrome

## Out of scope (deliberately)

- Dark mode
- Article TOC
- Multi-column footer
- Custom syntax highlighting theme (uses Pelican's default Pygments theme)
