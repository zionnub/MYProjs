#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:29:31 2020

@author: musingh
"""

from github import Github

# First create a Github instance:


# or using an access token
g = Github("9d28771a33fee5332867e4b043fd8b29f05acb3a")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
    
    
import requests

user = "mks-noon"
token = "9d28771a33fee5332867e4b043fd8b29f05acb3a"
repo = "catalog-content"

url ="https://api.github.com/repos/fastfishio/catalog-content/git/trees/live?recursive=1"

r = requests.get(url,auth=(user,token))
print(r.status_code)
res = r.json()

for file in res["tree"]:
    #print(file["path"])
    if(file["path"] =="noon/pages/desktop/big-yellow-sale.yml"):
        print(file['sha'])
    
url = "https://api.github.com/repos/fastfishio/catalog-content/git/blobs/cfdc8f4400428f84b40e977355ecf684f3a5c2da"

r = requests.get(url,auth=(user,token))
print(r.status_code)
res = r.json()
string = res['content']
res


import base64
decoded_yaml=base64.b64decode(string).decode('UTF-8')
decoded_yaml


#decoded_yaml = re.sub("\r", '', decoded_yaml)
#decoded_yaml = re.sub("\n", '', decoded_yaml)

decoded_yaml = re.sub("{% if country\('ae'\) %}", 'split country:ae', decoded_yaml)
decoded_yaml = re.sub("{% if country\('sa'\) %}", 'split country:sa', decoded_yaml)
decoded_yaml = re.sub("{% if country\('eg'\) %}", 'split country:eg', decoded_yaml)
decoded_yaml = re.sub("{% endif %}", '', decoded_yaml)

decoded_yaml = re.sub('{%', '', decoded_yaml)
decoded_yaml = re.sub('%}', '', decoded_yaml)
decoded_yaml = re.sub('{{', '', decoded_yaml)
decoded_yaml = re.sub('}}', '', decoded_yaml)


#re.sub("country:ae(\\r|\\n)*data:(\\r|\\n)*(\s)*-","abc -","country:ae\r\ndata:\r\n\r\n  - modules:\r\n")

decoded_yaml = re.sub("country:ae(\\r|\\n)*data:(\\r|\\n)*(\s)*", 'data:\r\n  - country: "ae" \r\n ', decoded_yaml)
decoded_yaml = re.sub("country:sa(\\r|\\n)*data:(\\r|\\n)*(\s)*", 'data:\r\n  - country: "sa" \r\n ', decoded_yaml)
decoded_yaml = re.sub("country:eg(\\r|\\n)*data:(\\r|\\n)*(\s)*", 'data:\r\n  - country: "eg" \r\n ', decoded_yaml)


#decoded_yaml = re.sub("country:ae\r\ndata:", '\r\ndata:\r\n\r\n  - country: "ae" \r\n', decoded_yaml)
#decoded_yaml = re.sub("country:sa\r\ndata:", '\r\ndata:\r\n\r\n  - country: "sa" \r\n', decoded_yaml)
#decoded_yaml = re.sub("country:eg\r\ndata:", '\r\ndata:\r\n\r\n  - country: "eg" \r\n', decoded_yaml)


all_country_yaml =decoded_yaml.split("split")

type(all_country_yaml)

for i in range(1,len(all_country_yaml)):



    temp_yaml=yaml.load(all_country_yaml[1],yaml.SafeLoader)
    type(temp_yaml['data'][0])
    country=temp_yaml['data'][0]['country']
    print(country)





k[3]

country,banner_type,widget_id,linkUrl,imageUrl,assetId

document = """
data:

  - bgColor: "#fff9f4"
    modules:

# title banner
    - type: bannerModuleStrip
      outerSpacing: {top: 0, bottom: 0}
      numPerRow: 1
      banners: 
      # - linkUrl: "/baby-breast-feeding"
      #   imageUrl: https://a.nooncdn.com/cms/pages/20200823/a609be75f9209272ff6565c61f39a4f1/{{lang()}}_banner-01.png
      #   assetId:  49937
      - linkUrl: "/baby-products"
        imageUrl: https://a.nooncdn.com/cms/pages/20200811/3e578ce0341c0ba93cdef0ff3ccdcfd6/{{lang()}}_slider-01.png
        assetId: 47757


#       - linkUrl: "/tommee_tippee?f[partner]=p_11"
#         imageUrl: https://a.nooncdn.com/cms/pages/20200728/f31a02613d66f2a4af2fd068f9c0f6e3/{{lang()}}_slider-01.jpg
#         assetId: 46870

      # - linkUrl: "/baby-products"
      #   imageUrl: https://a.nooncdn.com/cms/pages/20200724/9ae6584e14bb34af5f96c473d72216c1/{{lang()}}_banner-01.jpg

      # - linkUrl: "/new-arr-BA_06"
      #   imageUrl: https://a.nooncdn.com/cms/pages/20200730/6bb35832c04eeba5ae2b6749d513bfbe/{{lang()}}_banner-01.gif
      #   assetId: 47010


  - bgColor: "#fff9f4"
    modules:

# categories
    - type: bannerModule 
      widgetId: 2151
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 9
      banners:

      # - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/space-banner.png

      - linkUrl: "/baby-products/feeding-16153/breastfeeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200823/3dd9c9ba39c44a7bc732dcb1d6affc6a/{{lang()}}_category-03.png
        assetId: 49939

      - linkUrl: "/diapers-wipes-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-01.png
        assetId: 45337

      - linkUrl: "/creams-oils-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-02.png
        assetId: 45338

      - linkUrl: "/baby-products/bathing-and-skin-care/skin-care-24519/baby-shampoos"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-03.png
        assetId: 45339

      - linkUrl: "/baby-products/swings-jumpers-and-bouncers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-04.png
        assetId: 45340

      - linkUrl: "/baby-products/feeding-16153/bottle-feeding/bottles-17092"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-05.png
        assetId: 45341

      - linkUrl: "/baby-products/feeding-16153/teethers-pacifiers-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-06.png
        assetId: 45342

      - linkUrl: "/baby-products/diaper-bags-17618"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-07.png
        assetId: 45343

      - linkUrl: "/gifting-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-08.png
        assetId: 45344

      # - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/space-banner.png

#   - bgColor: "#fff9f4"
#     modules:

# # just landed
#     - type: bannerModule
#       widgetId: 2152
#       outerSpacing: {top: 5, bottom: 5}
#       numPerRow: 1
#       banners: 

#         - linkUrl: "/"
#           imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-02.gif
#           assetId: 45345

  - bgColor: "#fff9f4"
    modules:

#shop top deals

    - type: bannerModuleStrip
      numPerRow: 1
      outerSpacing: {top: 5, bottom: 1}
      banners:

      - imageUrl: https://a.nooncdn.com/cms/pages/20200826/79467ff0d55a066cd80223367f09fc4e/{{lang()}}_title-01.png
        
    - type: bannerModule
      widgetId: 2648
      numPerRow: 4
      outerSpacing: {top: 1, bottom: 7}
      banners:

      - linkUrl: "/baby-products/the_first_years"
        imageUrl: https://a.nooncdn.com/cms/pages/20200903/b314e46bdc6ed9ba04268f6cf8ff24d7/{{lang()}}_cat-module-01.png
        assetId: 51594

      - linkUrl: "/baby-products/rotho_babydesign"
        imageUrl: https://a.nooncdn.com/cms/pages/20200903/b314e46bdc6ed9ba04268f6cf8ff24d7/{{lang()}}_cat-module-02.png
        assetId: 51597

      - linkUrl: "/baby-products/hauck"
        imageUrl: https://a.nooncdn.com/cms/pages/20200903/b314e46bdc6ed9ba04268f6cf8ff24d7/{{lang()}}_cat-module-03.png
        assetId: 51598

      - linkUrl: "/baby-products/nip"
        imageUrl: https://a.nooncdn.com/cms/pages/20200903/b314e46bdc6ed9ba04268f6cf8ff24d7/{{lang()}}_cat-module-04.png
        assetId: 51599


    - type: bannerModule
      widgetId: 633
      outerSpacing: {top: 7, bottom: 7}
      numPerRow: 1
      banners: 

      - linkUrl: "/bp-coupon-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200903/23120f2721a51309b29b964888573ca4/{{lang()}}_strip-01.png
        assetId: 51636


# shop by category
    - type: bannerModuleStrip
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 1
      banners: 

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-01.jpg

  - bgColor: "#fff9f4"
    modules:

# diapering
    - type: bannerModuleStrip
      widgetId: 2157
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-products/diapering"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-04.jpg
        assetId: 45356

    - type: bannerModule
      widgetId: 2158
      outerSpacing: {top: 0, bottom: 7}
      numPerRow: 3
      banners:

      - linkUrl: "/diapers-wipes-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-10.jpg
        assetId: 45357

      - linkUrl: "/baby-products/potty-training"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-11.jpg
        assetId: 45358

      - linkUrl: "/baby-products/diapering/diaper-bins-and-refills"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-12.jpg
        assetId: 45359

    - type: bannerModule
      outerSpacing: {top: 7, bottom: 7}
      widgetId: 2659
      numPerRow: 1
      banners:

      - linkUrl: "/babyjoy-mt-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200907/d46a8a1957c404a66fcf9495db371c2e/{{lang()}}_strip-01.gif
        assetId: 51843


  - bgColor: "#fff9f4"
    modules:

# nursing & feeding
    - type: bannerModuleStrip
      widgetId: 2155
      outerSpacing: {top: 0, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/feeding-nursing"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-03.jpg
        assetId: 45350

    - type: bannerModule
      widgetId: 2156
      outerSpacing: {top: 0, bottom: 0}
      numPerRow: 3
      banners:

      - linkUrl: "/baby-products/feeding-16153/bottle-feeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-04.jpg
        assetId: 45351

      - linkUrl: "/baby-products/feeding-16153/breastfeeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-05.jpg
        assetId: 45395

      - linkUrl: "/baby-products/feeding-16153/highchairs-and-booster-seats"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-06.jpg
        assetId: 45352

      - linkUrl: "/baby-products/feeding-16153/solid-feeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-07.jpg
        assetId: 45353

      - linkUrl: "/grocery-store/baby-foods"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-08.jpg
        assetId: 45354

      - linkUrl: "/baby-products/feeding-16153/Bibs%20&%20Burp%20Cloths"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-09.jpg
        assetId: 45355


    # - type: bannerModule
    #   outerSpacing: {top: 7, bottom: 0}
    #   widgetId: 2499
    #   numPerRow: 1
    #   banners:

    #   - linkUrl: "/medela-coupon-BA_06"
    #     imageUrl: https://a.nooncdn.com/cms/pages/20200822/603c3c42189bfa8e6dcd907b47f33ac5/{{lang()}}_banner-02.png
    #     assetId: 49786


  - bgColor: "#fff9f4"
    modules:

# baby transport
    - type: bannerModuleStrip
      widgetId: 2153
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-transport"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-02.jpg
        assetId: 45346

    - type: bannerModule
      widgetId: 2154
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/strollers-prams"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-01.jpg
        assetId: 45347

      - linkUrl: "/baby-products/baby-transport/car-seats"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-02.jpg
        assetId: 45348

      - linkUrl: "/baby-products/baby-transport/carrier-and-slings"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-03.jpg
        assetId: 45349

  - bgColor: "#fff9f4"
    modules:

# bathing & skin care
    - type: bannerModuleStrip
      widgetId: 2159
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-products/bathing-and-skin-care"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-05.jpg
        assetId: 45360

    - type: bannerModule
      widgetId: 2160
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/baby-products/bathing-and-skin-care/skin-care-24519"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-13.jpg
        assetId: 45361

      - linkUrl: "/lotions-creams-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-14.jpg
        assetId: 45362

      - linkUrl: "/baby-products/bathing-and-skin-care/grooming-and-healthcare-kits"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-15.jpg
        assetId: 45363

  - bgColor: "#fff9f4"
    modules:

# health & safety
    - type: bannerModuleStrip
      widgetId: 2161
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/health-safety-baby"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-06.jpg
        assetId: 45364

    - type: bannerModule
      widgetId: 2162
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 4
      banners:

      - linkUrl: "/baby-products/safety-17316/monitors-18094"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-16.jpg
        assetId: 45365

      - linkUrl: "/baby-products/bathing-and-skin-care/baby-thermometers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-17.jpg
        assetId: 45366

      - linkUrl: "/baby-products/feeding-16153/bottle-feeding/feeding-sterilizers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-18.jpg
        assetId: 45367

      - linkUrl: "/baby-products/safety-17316/gates-and-doorways"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-19.jpg
        assetId: 45368

  - bgColor: "#fff9f4"
    modules:

# entertainment
    - type: bannerModuleStrip
      widgetId: 2163
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/entertainment-all-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-07.jpg
        assetId: 45369

    - type: bannerModule
      widgetId: 2164
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/toys-and-games/baby-and-toddler-toys?f[is_fbn]=1"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-20.jpg
        assetId: 45370

      - linkUrl: "/gifting-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-21.jpg
        assetId: 45371

      - linkUrl: "/baby-shower-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-22.jpg
        assetId: 45372

  - bgColor: "#fff9f4"
    modules:

# organic skin care
    - type: bannerModule
      widgetId: 2165
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 1
      banners: 

        - linkUrl: "/organic-BA_06"
          imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-03.jpg
          assetId: 45373

  - bgColor: "#fff9f4"
    modules:

# mums & mums-to-be
    - type: bannerModuleStrip
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-08.jpg

    - type: bannerModule
      widgetId: 2166
      outerSpacing: {top: 0, bottom: 0}
      numPerRow: 4
      banners:

      - linkUrl: "/fashion/women-31229/clothing-16021/maternity-16024"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-23.jpg
        assetId: 45374

      - linkUrl: "/mum-pc-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-24.jpg
        assetId: 45375

      - linkUrl: "/baby-products/feeding-16153/breastfeeding/breast_care"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-25.jpg
        assetId: 45376

      - linkUrl: "/baby-products/diaper-bags-17618"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-26.jpg
        assetId: 45377

  - bgColor: "#fff9f4"
    modules:

# parenting essentials
    - type: bannerModule
      widgetId: 2167
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 1
      banners:

      - linkUrl: "/parenting-essentials-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200724/9ae6584e14bb34af5f96c473d72216c1/{{lang()}}_cat-module-27.jpg
        assetId: 45378


  - bgColor: "#fff9f4"
    modules:

# fashion
    - type: bannerModule
      widgetId: 2168
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

        - linkUrl: "/view-all-kids-clothing"
          imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-04.jpg
          assetId: 45379

  - bgColor: "#fff9f4"
    modules:

# fashion categories
    - type: bannerModule
      widgetId: 2169
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 5
      banners:

      - imageUrl: https://a.nooncdn.com/cms/pages/20190923/53ac2a8338f3484edc51d05bafd5e99a/space-banner.png

      - linkUrl: "/baby-products/clothing-shoes-and-accessories"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-28.jpg
        assetId: 45380

      # - linkUrl: "/baby-clothing-sets"
      #   imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-29.jpg
      #   assetId: 45381

      - linkUrl: "/fashion/girls-31223"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-30.jpg
        assetId: 45382

      - linkUrl: "/fashion/boys-31221"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-31.jpg
        assetId: 45383

      - imageUrl: https://a.nooncdn.com/cms/pages/20190923/53ac2a8338f3484edc51d05bafd5e99a/space-banner.png


#   - bgColor: "#fff9f4"
#     modules:

# # real mum's favourites
#     - type: bannerModule
#       widgetId: 2170
#       outerSpacing: {top: 5, bottom: 5}
#       numPerRow: 1
#       banners: 

#         - linkUrl: "/"
#           imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-05.jpg
#           assetId: 45384

  - bgColor: "#fff9f4"
    modules:

# featured brands
    - type: bannerModuleStrip
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-09.jpg

    - type: bannerModule
      widgetId: 2171
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 5
      banners:

      - linkUrl: "/waterwipes"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-01.jpg
        assetId: 45385

      - linkUrl: "/pampers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-02.jpg
        assetId: 45386

      - linkUrl: "/babyjoy"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-03.jpg
        assetId: 45387

      - linkUrl: "/baby-products/braun"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-04.jpg
        assetId: 45388

      - linkUrl: "/mustela"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-05.jpg
        assetId: 45389

      - linkUrl: "/baby_plus"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-06.jpg
        assetId: 45390

      - linkUrl: "/babytrend"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-07.jpg
        assetId: 45391

      - linkUrl: "/baby-products/johnson_s"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-08.jpg
        assetId: 45392

      - linkUrl: "/chicco"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-09.jpg
        assetId: 45393

      - linkUrl: "/tommee_tippee"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-10.jpg
        assetId: 45394 


  - modules:
    - type: staticNavigation
      sections: {{ nav('baby') }}








data:

  - bgColor: "#fff9f4"
    modules:

# title banner
    - type: bannerSlider
      outerSpacing: {top: 0, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-products"
        imageUrl: https://a.nooncdn.com/cms/pages/20200811/3e578ce0341c0ba93cdef0ff3ccdcfd6/{{lang()}}_slider-01.png
        assetId: 47758

      # - linkUrl: "/baby-products"
      #   imageUrl: https://a.nooncdn.com/cms/pages/20200724/9ae6584e14bb34af5f96c473d72216c1/{{lang()}}_banner-01.jpg

      - linkUrl: "/bebi-store"
        imageUrl: https://a.nooncdn.com/cms/pages/20200825/28858f17e7ec520731d1389f9185f89f/{{lang()}}_slider-02.gif
        assetId: 44077



  - bgColor: "#fff9f4"
    modules:

# categories
    - type: bannerModule 
      widgetId: 2151
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 10
      banners:

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/space-banner.png

      - linkUrl: "/diapers-wipes-sa-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-01.png
        assetId: 46675

      - linkUrl: "/creams-oils-sa-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-02.png
        assetId: 46676

      - linkUrl: "/baby-products/bathing-and-skin-care/skin-care-24519/baby-shampoos"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-03.png
        assetId: 46677

      - linkUrl: "/baby-products/swings-jumpers-and-bouncers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-04.png
        assetId: 46678

      - linkUrl: "/baby-products/feeding-16153/bottle-feeding/bottles-17092"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-05.png
        assetId: 46679

      - linkUrl: "/teethers-pacifiers-sa-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-06.png
        assetId: 46680

      - linkUrl: "/baby-products/diaper-bags-17618"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-07.png
        assetId: 46681

      - linkUrl: "/gifting-baby-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200723/5d0d8d0b8528a37ebbec0a75cbc748d4/{{lang()}}_category-08.png
        assetId: 46682

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/space-banner.png

#   - bgColor: "#fff9f4"
#     modules:

# # just landed
#     - type: bannerModule
#       widgetId: 2152
#       outerSpacing: {top: 5, bottom: 5}
#       numPerRow: 1
#       banners: 

#         - linkUrl: "/"
#           imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-02.gif
#           assetId: 45345





# shop top deals
#   - bgColor: "#fff9f4"
#     modules:
#     - type: bannerModuleStrip
#       outerSpacing: {top: 5, bottom: 0}
#       numPerRow: 1
#       banners: 

#       - imageUrl: https://a.nooncdn.com/cms/pages/20200819/68c57af5394caa4758b7c004f7806c61/{{lang()}}_title-01.png

#     - type: bannerModule
#       widgetId: 
#       outerSpacing: {top: 0, bottom: 5}
#       numPerRow: 4
#       banners: 

#       - linkUrl: "/babytrend-deal-BA_06"
#         imageUrl: https://a.nooncdn.com/cms/pages/20200819/a9f4416f7656d5681016db9ca9f46385/{{lang()}}_cat-module-01.png
#         # imageUrl: https://a.nooncdn.com/cms/pages/20200819/68c57af5394caa4758b7c004f7806c61/{{lang()}}_cat-module-01.png
#         assetId: 49271
#       - linkUrl: "/sauvinex-deals-BA_06"
#         imageUrl: https://a.nooncdn.com/cms/pages/20200819/68c57af5394caa4758b7c004f7806c61/{{lang()}}_cat-module-02.png
#         assetId: 49272
#       - linkUrl: "/lovi-deal-BA_06"
#         imageUrl: https://a.nooncdn.com/cms/pages/20200819/68c57af5394caa4758b7c004f7806c61/{{lang()}}_cat-module-03.png
#         assetId: 49273
#       - linkUrl: "/canpol-deal-BA_06"
#         imageUrl: https://a.nooncdn.com/cms/pages/20200819/68c57af5394caa4758b7c004f7806c61/{{lang()}}_cat-module-04.png
#         assetId: 49274


  - bgColor: "#fff9f4"
    modules:

# shop by category
    - type: bannerModuleStrip
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-01.jpg


  - bgColor: "#fff9f4"
    modules:

# nursing & feeding
    - type: bannerModuleStrip
      widgetId: 2155
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/feeding-nursing"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-03.jpg
        assetId: 46687

    - type: bannerModule
      widgetId: 2156
      outerSpacing: {top: 0, bottom: 7}
      numPerRow: 5
      banners:

      - linkUrl: "/baby-products/feeding-16153/bottle-feeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_mb-cat-module-04.jpg
        assetId: 46688

      - linkUrl: "/baby-products/feeding-16153/breastfeeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_mb-cat-module-05.jpg
        assetId: 46689

      - linkUrl: "/baby-products/feeding-16153/highchairs-and-booster-seats"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_mb-cat-module-06.jpg
        assetId: 46690

      - linkUrl: "/baby-products/feeding-16153/solid-feeding"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_mb-cat-module-07.jpg
        assetId: 46691

      - linkUrl: "/baby-products/feeding-16153/Bibs%20&%20Burp%20Cloths"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_mb-cat-module-09.jpg
        assetId: 46692

  - bgColor: "#fff9f4"
    modules:

# baby transport
    - type: bannerModuleStrip
      widgetId: 2153
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-transport"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-02.jpg
        assetId: 46683

    - type: bannerModule
      widgetId: 2154
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/strollers-prams"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-01.jpg
        assetId: 46684

      - linkUrl: "/baby-products/baby-transport/car-seats"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-02.jpg
        assetId: 46685

      - linkUrl: "/baby-products/baby-transport/carrier-and-slings"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-03.jpg
        assetId: 46686





  - bgColor: "#fff9f4"
    modules:

# diapering
    - type: bannerModuleStrip
      widgetId: 2157
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-products/diapering"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-04.jpg
        assetId: 46693

    - type: bannerModule
      widgetId: 2158
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/diapers-wipes-sa-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-10.jpg
        assetId: 46694

      - linkUrl: "/baby-products/potty-training"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-11.jpg
        assetId: 46695

      - linkUrl: "/baby-products/diapering/diaper-bins-and-refills"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-12.jpg
        assetId: 46696

  - bgColor: "#fff9f4"
    modules:

# bathing & skin care
    - type: bannerModuleStrip
      widgetId: 2159
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/baby-products/bathing-and-skin-care"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-05.jpg
        assetId: 46697

    - type: bannerModule
      widgetId: 2160
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/baby-products/bathing-and-skin-care/skin-care-24519"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-13.jpg
        assetId: 46698

      - linkUrl: "/lotions-creams-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-14.jpg
        assetId: 46699

      - linkUrl: "/baby-products/bathing-and-skin-care/grooming-and-healthcare-kits"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-15.jpg
        assetId: 46700

  - bgColor: "#fff9f4"
    modules:

# health & safety
    - type: bannerModuleStrip
      widgetId: 2161
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/health-safety-baby"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-06.jpg
        assetId: 46701

    - type: bannerModule
      widgetId: 2162
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 4
      banners:

      - linkUrl: "/baby-products/safety-17316/monitors-18094"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-16.jpg
        assetId: 46702

      - linkUrl: "/baby-products/bathing-and-skin-care/baby-thermometers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-17.jpg
        assetId: 46703

      - linkUrl: "/baby-products/feeding-16153/bottle-feeding/feeding-sterilizers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-18.jpg
        assetId: 46704

      - linkUrl: "/baby-products/safety-17316/gates-and-doorways"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-19.jpg
        assetId: 46705

  - bgColor: "#fff9f4"
    modules:

# entertainment
    - type: bannerModuleStrip
      widgetId: 2163
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - linkUrl: "/entertainment-all-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-07.jpg
        assetId: 46706

    - type: bannerModule
      widgetId: 2164
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 3
      banners:

      - linkUrl: "/toys-and-games/baby-and-toddler-toys?f[is_fbn]=1"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-20.jpg
        assetId: 46707

      - linkUrl: "/gifting-baby-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-21.jpg
        assetId: 46708

      - linkUrl: "/baby-shower-sa-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-22.jpg
        assetId: 46709

  - bgColor: "#fff9f4"
    modules:

# organic skin care
    - type: bannerModule
      widgetId: 2165
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 1
      banners: 

        - linkUrl: "/organic-BA_06"
          imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-03.jpg
          assetId: 46710

  - bgColor: "#fff9f4"
    modules:

# mums & mums-to-be
    - type: bannerModuleStrip
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-08.jpg

    - type: bannerModule
      widgetId: 2166
      outerSpacing: {top: 0, bottom: 0}
      numPerRow: 4
      banners:

      - linkUrl: "/fashion/women-31229/clothing-16021/maternity-16024"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-23.jpg
        assetId: 46711

      - linkUrl: "/mum-pc-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-24.jpg
        assetId: 46712

      - linkUrl: "/baby-products/feeding-16153/breastfeeding/breast_care"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-25.jpg
        assetId: 46713

      - linkUrl: "/baby-products/diaper-bags-17618"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-26.jpg
        assetId: 46714

  - bgColor: "#fff9f4"
    modules:

# parenting essentials
    - type: bannerModule
      widgetId: 2167
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 1
      banners:

      - linkUrl: "/parenting-essentials-sa-BA_06"
        imageUrl: https://a.nooncdn.com/cms/pages/20200724/9ae6584e14bb34af5f96c473d72216c1/{{lang()}}_cat-module-27.jpg
        assetId: 46715


  - bgColor: "#fff9f4"
    modules:

# fashion
    - type: bannerModule
      widgetId: 2168
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

        - linkUrl: "/view-all-kids-clothing"
          imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_banner-04.jpg
          assetId: 46716

  - bgColor: "#fff9f4"
    modules:

# fashion categories
    - type: bannerModule
      widgetId: 2169
      outerSpacing: {top: 5, bottom: 5}
      numPerRow: 5
      banners:

      - imageUrl: https://a.nooncdn.com/cms/pages/20190923/53ac2a8338f3484edc51d05bafd5e99a/space-banner.png

      - linkUrl: "/baby-products/clothing-shoes-and-accessories"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-28.jpg
        assetId: 46717

      - linkUrl: "/fashion/girls-31223"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-30.jpg
        assetId: 46718

      - linkUrl: "/fashion/boys-31221"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_cat-module-31.jpg
        assetId: 46719

      - imageUrl: https://a.nooncdn.com/cms/pages/20190923/53ac2a8338f3484edc51d05bafd5e99a/space-banner.png


  - bgColor: "#fff9f4"
    modules:

# featured brands
    - type: bannerModuleStrip
      outerSpacing: {top: 5, bottom: 0}
      numPerRow: 1
      banners: 

      - imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/{{lang()}}_title-09.jpg

    - type: bannerModule
      widgetId: 2171
      outerSpacing: {top: 0, bottom: 5}
      numPerRow: 5
      banners:

      - linkUrl: "/waterwipes"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-01.jpg
        assetId: 46720

      - linkUrl: "/pampers"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-02.jpg
        assetId: 46721

      - linkUrl: "/babyjoy"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-03.jpg
        assetId: 46722

      - linkUrl: "/bebi"
        imageUrl: https://a.nooncdn.com/cms/pages/20200812/62723653f9c936067ee5490debe8e5d6/en_brand-module-08.png
        assetId: 48355

      - linkUrl: "/mustela"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-05.jpg
        assetId: 46724

      - linkUrl: "/baby_plus"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-06.jpg
        assetId: 46725

      - linkUrl: "/babytrend"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-07.jpg
        assetId: 46726

      - linkUrl: "/baby-products/johnson_s"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-08.jpg
        assetId: 46727

      - linkUrl: "/chicco"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-09.jpg
        assetId: 46728

      - linkUrl: "/tommee_tippee"
        imageUrl: https://a.nooncdn.com/cms/pages/20200722/8d0806207e544065436444c1a418da1b/en_brand-module-10.jpg
        assetId: 46729 


  - modules:
    - type: staticNavigation
      sections: {{ nav('baby') }}



data:


  - bgColor: "#ffffff"
    bgImage: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/desktop_bg.png

    modules:

    - type: bannerSlider
      outerSpacing: {top: 0, bottom: 2}
      numPerRow: 1
      banners:
      - linkUrl: "/toys-and-games/sports-and-outdoor-play/pools-and-water-fun"
        imageUrl: https://a.nooncdn.com/cms/pages/20200823/29ef853588879bad7959e1aab53ce989/{{lang()}}_banner-03.png
        assetId: 49933      
      - linkUrl: "/p-23258"
        imageUrl: https://a.nooncdn.com/cms/pages/20200816/ede705ce96beaada8193619dcd35eef8/{{lang()}}_banner-01.png
        assetId: 48715
      - linkUrl: "/baby-products/bathing-and-skin-care/skin-care-24519/baby-sun-protection"
        imageUrl: https://a.nooncdn.com/cms/pages/20200719/1fff04023c3a061e17e30f4fae240751/{{lang()}}_banner-05.png
        assetId: 45112                          
      - imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_banner-01.jpg
        linkUrl: "/baby-products"
        assetId: 9294

    - type: productCarousel
      outerSpacing: {top: 5, bottom: 10}
      productUrl: "/baby-products?f[is_fbn]=1&sort[by]=new_arrivals&sort[dir]=desc"
      moduleHeader:
        titleText: {% if lang('en') %} New Arrivals {% else %} وصل حديثاً  {% endif %}
        linkText: {% if lang('en') %}Shop Now{% else %}تسوق الآن{% endif %}
        linkUrl: "/baby-products?f[is_fbn]=1&sort[by]=new_arrivals&sort[dir]=desc"

    - type: bannerModule

      outerSpacing: {top: 5, bottom: 7}
      numPerRow: 2

      banners:
      - linkUrl: "/baby-products/baby-transport/standard"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_cat-module-01.png
        assetId: 9277
      - linkUrl: "/baby-products/car-seats-and-accessories/car-seats?sort[by]=price&sort[dir]=desc"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_cat-module-02.png
        assetId: 9278
      - linkUrl: "/baby-products/diapering"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_cat-module-03.png
        assetId: 9279
      - linkUrl: "/feeding-16153"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_cat-module-04.png
        assetId: 9280
      - linkUrl: "/baby-products/bathing-and-skin-care"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_cat-module-05.png
        assetId: 9281
      - linkUrl: "/baby-nursey-safety"
        imageUrl: https://a.nooncdn.com/cms/pages/20190920/f7a6e713b77e37fb2840a636179e6e7b/{{lang()}}_cat-module-06.png
        assetId: 9282


    - type: productCarousel
      outerSpacing: {top: 4, bottom: 7}
      productUrl: "/baby-eg"
      moduleHeader:
         #titleColor: "#000000"
         titleText: {% if lang('en') %}  Baby Care - Up to 30%  {% else %}  منتجات الأطفال - خصم حتى 30%  {% endif %}
         linkText: {% if lang('en') %}VIEW ALL{% else %}عرض الكل{% endif %}
         linkUrl: "/baby-eg"

    - type: productCarousel
      outerSpacing: {top: 7, bottom: 7}
      productUrl: "/diapers-eg"
      moduleHeader:
         #titleColor: "#000000"
         titleText: {% if lang('en') %}  Diapers - Up to 20%  {% else %} حفاضات - خصم حتى 20%  {% endif %}
         linkText: {% if lang('en') %}VIEW ALL{% else %}عرض الكل{% endif %}
         linkUrl: "/diapers-eg"



    - type: bannerModule
      outerSpacing: {top: 5, bottom: 7}
      numPerRow: 1
      banners:
      - imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/{{lang()}}_cat-module-07.jpg
        linkUrl: "/hamleys"
        assetId: 9292




    - type: bannerModule
      outerSpacing: {top: 7, bottom: 9}
      moduleHeader:
         titleText: {% if lang('en') %} SHOP BY BRAND   {% else %} تسوق حسب الماركة     {% endif %}
      numPerRow: 9
      banners:

      - linkUrl: "/baby-products/chicco"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-01.jpg
        assetId: 9283
      - linkUrl: "/baby-products/lovi"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-02.jpg
        assetId: 9284
      - linkUrl: "/baby-products/johnson_s"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-03.jpg
        assetId: 9285
      - linkUrl: "/baby-products/philips_avent"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-04.jpg
        assetId: 9286
      - linkUrl: "/baby-products/munchkin"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-05.jpg
        assetId: 9287
      - linkUrl: "/baby-products/dr_browns"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-06.jpg
        assetId: 9293
      - linkUrl: "/baby-products/baby_jem"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-07.jpg
        assetId: 9288
      - linkUrl: "/baby-products/canpol"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-08.jpg
        assetId: 9289
      - linkUrl: "/baby-products/pampers"
        imageUrl: https://a.nooncdn.com/cms/pages/20190611/c7dc8f07ea4c2816d3c1a1e525f1e174/en_brand-module-09.jpg
        assetId: 9290
"""

import re

document = re.sub('{%', '', document)
document = re.sub('%}', '', document)
document = re.sub('{{', '', document)
document = re.sub('}}', '', document)
{% endif %}



k=yaml.load(document,yaml.SafeLoader)
type(k['data'][0]['modules'])

for 




for i in k['data'][0]['modules'][0]['banners']:
    print(i['linkUrl'])
    print(i['assetId'])


for data_row in k['data']:
    for module_row in data_row['modules']:
        if(module_row['type'] in ('bannerSlider','bannerModule')):
            
            module_type = module_row['type']
            print(module_type)
            try:
                widget_id=module_row['widgetId']
                print(widget_id)
    
            except:
                widget_id=None
                
            for banners in module_row['banners']:
                try:
                    linkUrl=banners['linkUrl']
                    print(linkUrl)
    
                except:
                    linkUrl=None
                
                try:
                    assetId=banners['assetId']
                    print(assetId)
    
                except:
                    assetId=None
                
                try:
                    imageUrl=banners['imageUrl']
                    print(imageUrl)
    
                except:
                    imageUrl=None
                
                temp_row = dict({'module_type':module_type,'widget_id':widget_id
                                ,'linkUrl':linkUrl,'assetId':assetId,'imageUrl':imageUrl})
            
        

import yaml