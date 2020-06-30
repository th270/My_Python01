
import requests

response=requests.get("https://timgsa.baidu.com/timg?"
                      "image&quality=80"
                      "&size=b9999_10000"
                      "&sec=1589822196311"
                      "&di=275aa26e98afcf403a9d94a790b55d21"
                      "&imgtype=0"
                      "&src=http%3A%2F%2Fi0.chexun.net%2Fi%2FDealersShop%2FUploads%2F2017%2F8%2Fdealer_default_35a345beec4a4c63b54f42ce93c2c5aa.jpg")
pic = open ('photo.jpg','wb')
pic.write(response.content)

