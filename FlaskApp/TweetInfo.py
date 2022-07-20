import requests
from requests.structures import CaseInsensitiveDict
import datetime
import json


def getTweetId(start,end): #Start and end must be string formatted as YYYY-MM-DD
        
    url = "https://twitter.com/i/api/2/search/adaptive.json?q=hello%20until%3A"+end+"%20since%3A"+start+"&count=10&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CsuperFollowMetadata"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Authorization"] = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    headers["Accept-Encoding"] = "utf-8"
    headers["Accept-Language"] = "it-IT,it;q=0.9"
    headers["Host"] = "twitter.com"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    headers["Referer"] = "https://twitter.com/i/api/2/search/adaptive.json?q=hello%20until%3A"+end+"%20since%3A"+start+"&count=10&query_source=typed_query&f=top"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "twid=u%3D932117382; external_referer=padhuUp37ziB1mb6tX%2Bb05GcyPv53d7c|0|8e8t2xd8A2w%3D; eu_cn=1; _ga=GA1.2.93165480.1639041738; _gid=GA1.2.624505042.1639342382; at_check=true; mbox=PC#356c4b92035948ab99ab26deb086c9b7.37_0#1702335148|session#9b800e34a85e428d8104041bcb4dfc6b#1639392111; lang=it; ads_prefs=\"HBESAAA=\"; auth_token=1197de7f1670aeff6af547f787204d104bb45112; ct0=1c14d6dafd314555d45b39978613aa164733c7d7c5a22e74583bc35216c502120972f54087e58bd0dd44ce3660b7f01e48b0e92e83dee4fb8dd2b63be9101c41c55227bec7f84f09139b018036b255ee; dnt=1; guest_id=v1%3A163922447468807094; personalization_id=\"v1_bOpa2oUV2+4jwFYaGS9muQ==\"; kdt=tSBvp0r2ROjXGBMA28Ufyuy6RbKlZZxl5OPKpbJ7; _ga_34PHSZMC42=GS1.1.1639090308.4.1.1639090385.0; _gcl_au=1.1.1760713346.1639055237; des_opt_in=Y; guest_id_ads=v1%3A163904173559581403; guest_id_marketing=v1%3A163904173559581403"
    headers["x-twitter-active-user"] = "no"
    headers["x-twitter-client-language"] = "it"
    headers["x-csrf-token"] = "1c14d6dafd314555d45b39978613aa164733c7d7c5a22e74583bc35216c502120972f54087e58bd0dd44ce3660b7f01e48b0e92e83dee4fb8dd2b63be9101c41c55227bec7f84f09139b018036b255ee"
    headers["x-twitter-auth-type"] = "OAuth2Session"
    resp = requests.get(url, headers=headers)

    data= json.loads(resp.text)
    x = (data['globalObjects']['tweets']).keys()
    
    if(len(x)==0):
        print("Chosing another tweet as base")
        #try with a different keyword     
        url = "https://twitter.com/i/api/2/search/adaptive.json?q=love%20until%3A"+end+"%20since%3A"+start+"&count=10&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CsuperFollowMetadata"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "*/*"
        headers["Authorization"] = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        headers["Accept-Encoding"] = "utf-8"
        headers["Accept-Language"] = "it-IT,it;q=0.9"
        headers["Host"] = "twitter.com"
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
        headers["Referer"] = "https://twitter.com/i/api/2/search/adaptive.json?q=hello%20until%3A"+end+"%20since%3A"+start+"&count=10&query_source=typed_query&f=top"
        headers["Connection"] = "keep-alive"
        headers["Cookie"] = "twid=u%3D932117382; external_referer=padhuUp37ziB1mb6tX%2Bb05GcyPv53d7c|0|8e8t2xd8A2w%3D; eu_cn=1; _ga=GA1.2.93165480.1639041738; _gid=GA1.2.624505042.1639342382; at_check=true; mbox=PC#356c4b92035948ab99ab26deb086c9b7.37_0#1702335148|session#9b800e34a85e428d8104041bcb4dfc6b#1639392111; lang=it; ads_prefs=\"HBESAAA=\"; auth_token=1197de7f1670aeff6af547f787204d104bb45112; ct0=1c14d6dafd314555d45b39978613aa164733c7d7c5a22e74583bc35216c502120972f54087e58bd0dd44ce3660b7f01e48b0e92e83dee4fb8dd2b63be9101c41c55227bec7f84f09139b018036b255ee; dnt=1; guest_id=v1%3A163922447468807094; personalization_id=\"v1_bOpa2oUV2+4jwFYaGS9muQ==\"; kdt=tSBvp0r2ROjXGBMA28Ufyuy6RbKlZZxl5OPKpbJ7; _ga_34PHSZMC42=GS1.1.1639090308.4.1.1639090385.0; _gcl_au=1.1.1760713346.1639055237; des_opt_in=Y; guest_id_ads=v1%3A163904173559581403; guest_id_marketing=v1%3A163904173559581403"
        headers["x-twitter-active-user"] = "no"
        headers["x-twitter-client-language"] = "it"
        headers["x-csrf-token"] = "1c14d6dafd314555d45b39978613aa164733c7d7c5a22e74583bc35216c502120972f54087e58bd0dd44ce3660b7f01e48b0e92e83dee4fb8dd2b63be9101c41c55227bec7f84f09139b018036b255ee"
        headers["x-twitter-auth-type"] = "OAuth2Session"
        resp = requests.get(url, headers=headers)
        data= json.loads(resp.text)
        x = (data['globalObjects']['tweets']).keys()
        
    list = []
    for key in x:
        list.append(key)
    return list[0]#just return the first tweet id retrieved from the json