import os
import random
import urllib.parse

import requests
from bs4 import BeautifulSoup





def build_path_image(img_url, dir_Path):  # build path for img. # 1
    img_name = img_url.rsplit('/', 1)[1]
    path_img = f"{dir_Path}/{img_name}"
    return path_img





def download_image(img_url, path_img):  # download image ftom.. to..# 2
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(path_img, 'wb') as f:
                f.write(response.content)
        else:
            pass
    except:
        pass


# x = 'https://en.wikipedia.org/wiki/Food'
# get_soup(x)


def get_soup(url):  # 7
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return (soup)




def title_in_wiki(url):  # to make subdirectories with appropriate name # 3
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            soup = get_soup(url)
            title = soup.title
            if title is not None:
                title_text = title.string.strip() if title.string else "Untitled"

                return ("", title_text)
        else:
            pass
    except:
        pass


# x = 'https://en.wikipedia.org/wiki/Food'
# title_in_wiki(x)

def mk_dir(path):  # 4
    try:
        os.mkdir(path)
    except:
        pass




def get_images(url, max_images):  # 5
    soup = get_soup(url)
    img_tags = soup.find_all('img', class_="mw-file-element")
    fixed_urls = []
    select_images = random.sample(img_tags, min(len(img_tags), max_images))
    for img in select_images:
        src = img.get('src')
        if src.startswith('//'):
            src = 'https:' + src
        elif src.startswith('/'):
            src = urllib.parse.urljoin(url, src)
        fixed_urls.append(src)
    return fixed_urls


# x = 'https://en.wikipedia.org/wiki/Food'
# y = 10
# get_images(x, y)


def select_links(url, max_links):  # 6
        soup = get_soup(url)
        link_tags = soup.find_all('a', href=True)
        fixed_links = set()
        get_links = random.sample(link_tags, min(len(link_tags),max_links))
        for link in get_links:
            href = link.get('href')
            if href.startswith('/wiki') and ':' not in href:
                fixed_links.add(urllib.parse.urljoin(url, href))
        return fixed_links



# x = 'https://en.wikipedia.org/wiki/Food'
# y = 10
# select_links(x, y)


# x = 'https://en.wikipedia.org/wiki/Food'
# y = 10
# get_images(x, y)


def recursive_crawling_wiki(url, max_images, max_links, depth):  # 8
    title = title_in_wiki(url)
    path_dir = '/home/mefathim-tech-56/mefathim/wiki-img'
    path_sub_dir = f"{path_dir}/{title}"
    mk_dir(path_sub_dir)
    images_to_download = get_images(url, max_images)
    for img in images_to_download:
        path_img = build_path_image(img, path_sub_dir)
        download_image(img, path_img)
        links_crawl = select_links(url, max_links)
        for link in links_crawl:
            if depth > 0:
                depth = depth - 1
                recursive_crawling_wiki(link, max_images, max_links, depth)





def main():
    x = 'https://en.wikipedia.org/wiki/Food'
    y = 10
    z = 5
    w = 3
    recursive_crawling_wiki(x, y, z, w)




if __name__ == '__main__':
    main()
