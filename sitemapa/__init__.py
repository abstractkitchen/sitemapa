import os
import gzip
import copy

from xml.etree import cElementTree


def get_xml_root(element, **kwargs):
    with_images = kwargs.get("with_images", False)
    with_videos = kwargs.get("with_videos", False)
    with_news = kwargs.get("with_news", False)

    root = cElementTree.Element(element)
    root.attrib['xmlns'] = "http://www.sitemaps.org/schemas/sitemap/0.9"

    if with_images:
        root.attrib["xmlns:image"] = "http://www.google.com/schemas/sitemap-image/1.1"

    if with_videos:
        root.attrib["xmlns:video"] = "http://www.google.com/schemas/sitemap-video/1.1"

    if with_news:
        root.attrib["xmlns:news"] = "http://www.google.com/schemas/sitemap-news/0.9"

    return root


def create_tags_from_dict(document, tag_name, tag_data):
    for element_property, element_property_value in tag_data.items():
        if not isinstance(element_property_value, dict):
            cElementTree.SubElement(
                document, f"{tag_name}:{element_property}").text = element_property_value

        else:
            if "$tags" in element_property_value:
                tags = element_property_value["$tags"]
                attrib = copy.deepcopy(element_property_value)
                attrib.pop("$tags")

                parent_tag = cElementTree.SubElement(
                    document, f"{tag_name}:{element_property}", attrib)

                create_tags_from_dict(parent_tag, tag_name, tags)
            else:
                value = element_property_value["$value"]
                attrib = copy.deepcopy(element_property_value)
                attrib.pop("$value")

                cElementTree.SubElement(
                    document, f"{tag_name}:{element_property}", attrib).text = value


# append extra tags inside <url>.
# this method is used to create <image:image>, <video:video>, <news:news>
def add_url_items(url_node, item_type, items):
    for element_data in items:
        document = cElementTree.SubElement(url_node, f"{item_type}:{item_type}")

        if not isinstance(element_data, dict):
            cElementTree.SubElement(document, f"{item_type}:loc").text = element_data

        else:

            # create more complex tags based on dict description
            create_tags_from_dict(document, item_type, element_data)


class SitemapBase:
    def __init__(self, **kwargs):
        max_urls = kwargs.get("max_urls", 50000)

        self.urls = {}
        self.max_urls = max_urls
        self.options = kwargs

        # These parameters will be detected automatically
        self.with_videos = False
        self.with_images = False
        self.with_news = False

    def create_tree(self):
        raise NotImplementedError

    def save(self, save_as, **kwargs):
        compress = ".xml.gz" in save_as
        root = self.create_tree()
        sitemap_name = save_as.split("/")[-1]
        dest_path = "/".join(save_as.split("/")[:-1])
        save_as = f"{dest_path}/{sitemap_name}"

        # create sitemap path if not existed
        if not os.path.exists(f"{dest_path}/"):
            os.makedirs(f"{dest_path}/")

        if not compress:
            tree = cElementTree.ElementTree(root)
            tree.write(save_as, encoding='utf-8', xml_declaration=True)
        else:
            gzipped_sitemap_file = gzip.open(save_as, 'wb')
            cElementTree.ElementTree(root).write(gzipped_sitemap_file)
            gzipped_sitemap_file.close()

        # reset urls
        self.urls = {}

        return sitemap_name


class Sitemap(SitemapBase):
    """
    This class is used to generate sitemaps(images, videos, urls, news)
    """

    def append_url(self, url, url_data=None):
        if url in self.urls:
            raise Exception(f"{url} already in sitemap data")

        if len(self.urls) == self.max_urls:
            raise Exception(f"You already have {self.max_urls} URLs. Time to save your sitemap.")

        if not url_data:
            url_data = {}

        # if any of these keys are presented in the sitemap settings,
        # then add new xmlns: attributes upon saving sitemap
        if "images" in url_data:
            self.with_images = True

        if "videos" in url_data:
            self.with_videos = True

        if "news" in url_data:
            self.with_news = True

        self.urls[url] = url_data

        return self.urls

    def create_tree(self):
        if not self.urls:
            raise Exception("Looks like you need to add some URLs first.")

        root = get_xml_root(
            "urlset",
            with_news=self.with_news,
            with_images=self.with_images,
            with_videos=self.with_videos
        )

        for url, url_data in self.urls.items():
            url_section = cElementTree.SubElement(root, "url")
            cElementTree.SubElement(url_section, "loc").text = url

            if "lastmod" in url_data:
                cElementTree.SubElement(url_section, "lastmod").text = url_data["lastmod"]

            # 'changefreq' and 'priority' are deprecated by Google
            if "changefreq" in url_data:
                cElementTree.SubElement(url_section, "changefreq").text = url_data["changefreq"]

            if "priority" in url_data:
                cElementTree.SubElement(url_section, "priority").text = url_data["priority"]

            if "images" in url_data:
                add_url_items(url_section, "image", url_data["images"])

            if "videos" in url_data:
                add_url_items(url_section, "video", url_data["videos"])

            if "news" in url_data:
                add_url_items(url_section, "news", url_data["news"])

        return root


class IndexSitemap(SitemapBase):
    def append_sitemap(self, sitemap_url, sitemap_data=None):
        if not sitemap_data:
            sitemap_data = {}

        self.urls[sitemap_url] = sitemap_data

        return self.urls

    def create_tree(self):
        if not self.urls:
            raise Exception("Looks like you need to add some URLs first.")

        root = get_xml_root("sitemapindex")

        for sitemap_url, sitemap_data in self.urls.items():
            sitemap_section = cElementTree.SubElement(root, "sitemap")
            cElementTree.SubElement(sitemap_section, "loc").text = sitemap_url

            if "lastmod" in sitemap_data:
                cElementTree.SubElement(sitemap_section, "lastmod").text = sitemap_data["lastmod"]

        return root
