#/usr/bin/python
import json, sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print >>sys.stderr, "%s [ad/gp] json_file" % (sys.argv[0])
    sys.exit(1);

  mode = sys.argv[1]
  
  ifile = open(sys.argv[2], "r")
  cnt = 0
  err_cnt = 0
  while True:
    cnt += 1
    #if cnt > 1:
    #  break
    if cnt % 1000 == 0:
      print >>sys.stderr, "%sK done" % str(cnt/1000)
    line = ifile.readline()
    if not line:
      break
    buff = line.strip()
    js = json.loads(buff)

    out = json.dumps(js, indent=2) 

    if mode == "ad":
      title = js["adTitle"].encode("UTF-8")
      title = title.replace("\r", " ")
      title = title.replace("\n", " ")
      desc = js["adDes"].encode("UTF-8")
      desc = desc.replace("\r", " ")
      desc = desc.replace("\n", " ")
      if (84975 == js["planId"]):
        print str(js["adId"]) \
            + "\t" + str(js["groupId"]) \
            + "\t" + str(js["planId"]) \
            + "\t" + str(js["userId"]) \
            + "\t" + title \
            + "\t" + desc
            #+ "\t" + js["showUrl"] \
            #+ "\t" + js["targetUrl"] 
    elif mode == "gp":
      kw = js["keyword"]
      for x in kw:
        bidword = x["word"].encode("UTF-8")
        if bidword.strip() != bidword:
          err_cnt += 1
          continue
        print str(js["gprice"]) \
            + "\t" + str(js["groupId"]) \
            + "\t" + str(js["planId"]) \
            + "\t" + str(js["userId"]) \
            + "\t" + bidword \
            + "\t" + str(x["bprice"]) \
            + "\t" + str(x["match_type"])
    else:
      break

  ifile.close()
  print >>sys.stderr, "final err cnt %s" % err_cnt


