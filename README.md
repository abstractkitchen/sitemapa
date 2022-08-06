# Sitemapa
#### _Create advanced sitemaps easily._

![Create sitemaps with Sitemapa](https://abstractkitchen.com/static/assets/sitemapa-image.jpg "Create sitemaps with Sitemapa")

Sitemapa is a small package to reduce your work while generating sitemaps. You describe your sitemaps with JSON-structure. Sitemapa is framework agnostic and not indexing your website — it's just generating sitemaps from your description. Noting more. I use it to generate sitemaps for millions of URLs on my websites. 

Keep in mind that it's your job to validate your urls and lastmod dates. [Learn more about sitemaps](https://developers.google.com/search/docs/advanced/sitemaps/overview) — it's important for your website SEO.

## Features
- No extra dependencies
- Create regular sitemaps. URLs, Images, Videos and News are supported.
- Create index sitemap to combine your regular sitemaps
- Create extra attributes for your tags like <video:restriction relationship="allow"> [video section](https://developers.google.com/search/docs/advanced/sitemaps/video-sitemaps#example-sitemap)
- Use JSON to describe your sitemaps. Don't waste your time with XML.
- Compress sitemaps with gzip

## Installation

```sh
pip install sitemapa

# import in your script
from sitemapa import Sitemap, IndexSitemap
```

## Usage

[Read about usage on my website](https://abstractkitchen.com/blog/sitemaps-for-devs/#sitemapa-library).

## Contacts
- [visit abstractkitchen.com](https://abstractkitchen.com)
- drop me a line: dmitry@abstractkitchen.com
- [connect with me on reddit](https://www.reddit.com/user/denisberezovsky)

## License

MIT
