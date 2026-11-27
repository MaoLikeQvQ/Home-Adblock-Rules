# 候选验证报告

状态：review-required

设备验收：未完成。实际内核结果见 engines.json。

## 审核项

### broad-24316c9a0f13ed56

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-KEYWORD,-ad.sm.cn),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-8d2c46880ff2dabd

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-KEYWORD,-ad.video.yximgs.com),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-15aab1f08790d1b3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-KEYWORD,-ad.wtzw.com),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-69f1f4fe9dcfc0c4

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-KEYWORD,-be-pack-sign.pglstatp-toutiao.com),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-af94376741575809

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,2o7.net),(NOT,((OR,((DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,vitacost.122.2o7.net))))))`

### broad-212469dffa6bc1d6

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,a8.net),(NOT,((DOMAIN-SUFFIX,px.a8.net))))`

### broad-022fdefb755dc7bf

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,adjust.com),(NOT,((OR,((DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,go.adjust.com))))))`

### broad-e630ba002c277af3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,ads.nicovideo.jp),(NOT,((DOMAIN-SUFFIX,res.ads.nicovideo.jp))))`

### broad-6d1786a8d113068a

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,ads.tvb.com),(NOT,((OR,((DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,img.ads.tvb.com))))))`

### broad-7560b59d89301742

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,amplitude.com),(NOT,((DOMAIN-SUFFIX,analytics.amplitude.com))))`

### broad-3dfc0c517584b091

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,analytics.edgekey.net),(NOT,((OR,((DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net))))))`

### broad-6289aa298b9c37a0

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,aniview.com),(NOT,((DOMAIN-SUFFIX,ssai.aniview.com))))`

### broad-45af90400f02c7ee

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,appcast.io),(NOT,((DOMAIN-SUFFIX,click.appcast.io))))`

### broad-636d51f9c177bfab

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,appmetrica.yandex.com),(NOT,((DOMAIN-SUFFIX,redirect.appmetrica.yandex.com))))`

### broad-241bd42c844ddf64

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,appodeal.com),(NOT,((DOMAIN-SUFFIX,artifactory.appodeal.com))))`

### broad-7e8a684024952d81

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,appsflyer.com),(NOT,((DOMAIN-SUFFIX,app.appsflyer.com))))`

### broad-fe38355063d18c40

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,bizrate.com),(NOT,((DOMAIN-SUFFIX,rd.bizrate.com))))`

### broad-20ac0ee88cb1754f

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,bluecore.com),(NOT,((DOMAIN-SUFFIX,s.bluecore.com))))`

### broad-54ae81d5cdcc11df

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,commander1.com),(NOT,((DOMAIN-SUFFIX,netatmo.commander1.com))))`

### broad-218679c8520a44de

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,conde.digital),(NOT,((DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital))))`

### broad-8103943feeb6307b

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,cptrack.de),(NOT,((DOMAIN-SUFFIX,click.cptrack.de))))`

### broad-db203da547087147

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,crwdcntrl.net),(NOT,((DOMAIN-SUFFIX,tags.crwdcntrl.net))))`

### broad-ddf9fed1d3a6d0c3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,dable.io),(NOT,((DOMAIN-SUFFIX,admin.dable.io))))`

### broad-0daa3ebaaac930f3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,datadoghq-browser-agent.com),(NOT,((DOMAIN-SUFFIX,www.datadoghq-browser-agent.com))))`

### broad-a2c1fdaf53ab7378

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,demdex.net),(NOT,((DOMAIN-SUFFIX,sbs.demdex.net))))`

### broad-bd76e2f875ab9833

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,dotomi.com),(NOT,((DOMAIN-SUFFIX,cj.dotomi.com))))`

### broad-7604b415fd45d59a

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,doubleclick.net),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,pagead.l.doubleclick.net))))))`

### broad-b274e75019df1c8a

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,ebis.ne.jp),(NOT,((OR,((DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp))))))`

### broad-6c523422fab73f9b

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,ec-optimizer.com),(NOT,((OR,((DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com))))))`

### broad-73f4833efb623a0d

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,exponea.com),(NOT,((DOMAIN-SUFFIX,public-cis.exponea.com))))`

### broad-e1db30acc1e3fd72

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,first-id.fr),(NOT,((DOMAIN-SUFFIX,gate.first-id.fr))))`

### broad-8841399f5d80aac0

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,gemius.pl),(NOT,((DOMAIN-SUFFIX,str.hit.gemius.pl))))`

### broad-e0598e192eb26a94

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,googleadservices.com),(NOT,((DOMAIN-SUFFIX,www.googleadservices.com))))`

### broad-b8693a084f2a3b03

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,hit.interia.pl),(NOT,((DOMAIN-SUFFIX,ia.hit.interia.pl))))`

### broad-142aa3eb5207738b

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,i2i.jp),(NOT,((DOMAIN-SUFFIX,id.i2i.jp))))`

### broad-0829857953779c41

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,in.treasuredata.com),(NOT,((DOMAIN-SUFFIX,ap01.records.in.treasuredata.com))))`

### broad-cd702354ab05f772

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,inmobi.com),(NOT,((DOMAIN-SUFFIX,cmp.inmobi.com))))`

### broad-104def1d525ddca0

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,jdoqocy.com),(NOT,((DOMAIN-SUFFIX,www.jdoqocy.com))))`

### broad-60ae25d58a379f58

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,link-ag.net),(NOT,((DOMAIN-SUFFIX,cl.link-ag.net))))`

### broad-f15f0dbb8746604d

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,metaffiliation.com),(NOT,((DOMAIN-SUFFIX,action.metaffiliation.com))))`

### broad-e0c9c9e81af625ef

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,mmstat.com),(NOT,((DOMAIN-SUFFIX,log.mmstat.com))))`

### broad-32835fc2cedd03ad

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,nakanohito.jp),(NOT,((OR,((DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp))))))`

### broad-eb81b7579a2091bd

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,newrelic.com),(NOT,((DOMAIN-SUFFIX,infra-api.newrelic.com))))`

### broad-2b25d914a882db81

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,openx.net),(NOT,((DOMAIN-SUFFIX,nineto5mac-d.openx.net))))`

### broad-f1dcd8474cf034c3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,optnx.com),(NOT,((DOMAIN-SUFFIX,s.optnx.com))))`

### broad-5557b02562a910fd

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,ownpage.fr),(NOT,((DOMAIN-SUFFIX,redir.ownpage.fr))))`

### broad-39f61c70d7f8bac5

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,peerius.com),(NOT,((DOMAIN-SUFFIX,intersport.peerius.com))))`

### broad-f102bb8678fd512a

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,perfdrive.com),(NOT,((DOMAIN-SUFFIX,validate.perfdrive.com))))`

### broad-c7738351abf0679b

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,redirectingat.com),(NOT,((DOMAIN-SUFFIX,go.redirectingat.com))))`

### broad-6bf03b939cbefa4d

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,researchnow.com),(NOT,((DOMAIN-SUFFIX,surveymyopinion.researchnow.com))))`

### broad-fdfa1506e0a92c83

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,roistat.com),(NOT,((DOMAIN-SUFFIX,stash.roistat.com))))`

### broad-adb7aafb548d7c61

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,rutarget.ru),(NOT,((DOMAIN-SUFFIX,track.rutarget.ru))))`

### broad-706d64193ae1a2ae

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,scarabresearch.com),(NOT,((DOMAIN-SUFFIX,recommender.scarabresearch.com))))`

### broad-646fa5867054cb6f

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,silverpop.com),(NOT,((DOMAIN-SUFFIX,cs.silverpop.com))))`

### broad-99940f646193843f

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,statcounter.com),(NOT,((OR,((DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,www.statcounter.com))))))`

### broad-b1d6d710f67cfc5b

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,targetspot.com),(NOT,((DOMAIN-SUFFIX,radiofrance.targetspot.com))))`

### broad-b7850c4e50e0daa3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,tealiumiq.com),(NOT,((DOMAIN-SUFFIX,my.tealiumiq.com))))`

### broad-7db13386ff1e6aaa

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,tr.line.me),(NOT,((DOMAIN-SUFFIX,oa.tr.line.me))))`

### broad-7790d1445803f10c

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,treasuredata.com),(NOT,((DOMAIN-SUFFIX,ap01.records.in.treasuredata.com))))`

### broad-8dcb289a91ba18b9

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,valuecommerce.ne.jp),(NOT,((OR,((DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp))))))`

### broad-ec9b9a98377836f2

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,viralize.tv),(NOT,((DOMAIN-SUFFIX,content.viralize.tv))))`

### broad-f145e6a75af3845e

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((DOMAIN-SUFFIX,webgains.com),(NOT,((DOMAIN-SUFFIX,track.webgains.com))))`

### broad-324a079a15bac50c

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,111.20.26.186/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-73d01349432645bd

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,112.84.130.73/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-cf7934ebe5f4ac4f

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,116.142.251.100/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-e279a3c4278e0cbf

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,116.177.251.215/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-d6f5846f5b59b0c3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,120.77.173.114/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-cb0cd04b4066f1ac

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,123.56.23.22/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-a70ea84f4bb91b48

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,14.29.101.160/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-a669398be5b56a32

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,14.29.101.168/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-b8e57e30f2ea207f

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,14.29.101.169/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-440bf465a162e607

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,182.254.116.116/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-1c276f478e28b72e

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,203.205.137.89/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-af5470dcb5cf37c2

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,218.77.192.51/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### broad-8f467eaa105cf8c3

New pattern, IP or compiled exception rule

- 目标：clash_block
- 规则：`AND,((IP-CIDR,38.190.225.166/32,no-resolve),(NOT,((OR,((DOMAIN-SUFFIX,5471782.fls.doubleclick.net),(DOMAIN-SUFFIX,79423.analytics.edgekey.net),(DOMAIN-SUFFIX,a.sellpoint.net),(DOMAIN-SUFFIX,aax-fe.amazon.co.jp),(DOMAIN-SUFFIX,ac.ebis.ne.jp),(DOMAIN-SUFFIX,acs-m.daraz.com.bd),(DOMAIN-SUFFIX,acs-m.daraz.pk),(DOMAIN-SUFFIX,action.metaffiliation.com),(DOMAIN-SUFFIX,ad.kazakinfo.com),(DOMAIN-SUFFIX,ad.ourgame.com),(DOMAIN-SUFFIX,adblock.adguard.com),(DOMAIN-SUFFIX,admin.dable.io),(DOMAIN-SUFFIX,admin.mailchimp.com),(DOMAIN-SUFFIX,adv.bloop.info),(DOMAIN-SUFFIX,advert.kf5.com),(DOMAIN-SUFFIX,afi-b.com),(DOMAIN-SUFFIX,alllaw.112.2o7.net),(DOMAIN-SUFFIX,analytics.amplitude.com),(DOMAIN-SUFFIX,analytics.cibc.com),(DOMAIN-SUFFIX,anwb.webpower.eu),(DOMAIN-SUFFIX,ap01.records.in.treasuredata.com),(DOMAIN-SUFFIX,api.ads.tvb.com),(DOMAIN-SUFFIX,api.docodoco.jp),(DOMAIN-SUFFIX,api.karte.io),(DOMAIN-SUFFIX,app-advertise.zhihuishu.com),(DOMAIN-SUFFIX,app.adjust.com),(DOMAIN-SUFFIX,app.appsflyer.com),(DOMAIN-SUFFIX,artifactory.appodeal.com),(DOMAIN-SUFFIX,awin1.com),(DOMAIN-SUFFIX,banner.dna.fi),(DOMAIN-SUFFIX,belgium.wolterskluwer.com),(DOMAIN-SUFFIX,c.office.com),(DOMAIN-SUFFIX,captcha.su.baidu.com),(DOMAIN-SUFFIX,catchup.thisisdax.com),(DOMAIN-SUFFIX,cbsi.map.fastly.net),(DOMAIN-SUFFIX,cdn.atmedia.hu),(DOMAIN-SUFFIX,cdn.datatables.net),(DOMAIN-SUFFIX,cdn.duurzaam.greenchoice.nl),(DOMAIN-SUFFIX,cdn.rozetka.com.ua),(DOMAIN-SUFFIX,chaturbate.com),(DOMAIN-SUFFIX,cindyholbrook.lpages.co),(DOMAIN-SUFFIX,citiintl.122.2o7.net),(DOMAIN-SUFFIX,cj.dotomi.com),(DOMAIN-SUFFIX,cl.link-ag.net),(DOMAIN-SUFFIX,classliving.lpages.co),(DOMAIN-SUFFIX,click.appcast.io),(DOMAIN-SUFFIX,click.avs.io),(DOMAIN-SUFFIX,click.cptrack.de),(DOMAIN-SUFFIX,click.simba.taobao.com),(DOMAIN-SUFFIX,click.trafficguard.ai),(DOMAIN-SUFFIX,click.virt.exacttarget.com),(DOMAIN-SUFFIX,clickattr.wayup.com),(DOMAIN-SUFFIX,cm-beacon.nakanohito.jp),(DOMAIN-SUFFIX,cm-widget.nakanohito.jp),(DOMAIN-SUFFIX,cmp.inmobi.com),(DOMAIN-SUFFIX,cmp.osano.com),(DOMAIN-SUFFIX,content.ingbank.pl),(DOMAIN-SUFFIX,content.viralize.tv),(DOMAIN-SUFFIX,crm-cdn.peek-cloppenburg.com),(DOMAIN-SUFFIX,cs.silverpop.com),(DOMAIN-SUFFIX,cutcaptcha.com),(DOMAIN-SUFFIX,daikoku.ebis.ne.jp),(DOMAIN-SUFFIX,data.digital.costco.ca),(DOMAIN-SUFFIX,data.digital.costco.com),(DOMAIN-SUFFIX,data.email.premierleague.com),(DOMAIN-SUFFIX,data.notify.macys.com),(DOMAIN-SUFFIX,data.orders.costco.ca),(DOMAIN-SUFFIX,data.orders.costco.com),(DOMAIN-SUFFIX,data.promo.timhortons.ca),(DOMAIN-SUFFIX,developers.google.com),(DOMAIN-SUFFIX,download.adguard.com),(DOMAIN-SUFFIX,e.customeriomail.com),(DOMAIN-SUFFIX,email.awscloud.com),(DOMAIN-SUFFIX,email.elitedangerous.com),(DOMAIN-SUFFIX,emails.educause.edu),(DOMAIN-SUFFIX,f-gear.ec-optimizer.com),(DOMAIN-SUFFIX,feed.adrelayer.com),(DOMAIN-SUFFIX,forum.notebookreview.com),(DOMAIN-SUFFIX,gate.first-id.fr),(DOMAIN-SUFFIX,get.neofinancial.com),(DOMAIN-SUFFIX,go.adjust.com),(DOMAIN-SUFFIX,go.redirectingat.com),(DOMAIN-SUFFIX,go.scorptec.com.au),(DOMAIN-SUFFIX,goto.target.com),(DOMAIN-SUFFIX,goto.walmart.com),(DOMAIN-SUFFIX,grp07.ias.rakuten.co.jp),(DOMAIN-SUFFIX,gs.statcounter.com),(DOMAIN-SUFFIX,hb.afl.rakuten.co.jp),(DOMAIN-SUFFIX,health.halodoc.com),(DOMAIN-SUFFIX,hidive.com),(DOMAIN-SUFFIX,home.focusatwill.com),(DOMAIN-SUFFIX,href.li),(DOMAIN-SUFFIX,ia.hit.interia.pl),(DOMAIN-SUFFIX,id.i2i.jp),(DOMAIN-SUFFIX,img.ads.tvb.com),(DOMAIN-SUFFIX,infra-api.newrelic.com),(DOMAIN-SUFFIX,injections.adguard.org),(DOMAIN-SUFFIX,intersport.peerius.com),(DOMAIN-SUFFIX,itoya.ec-optimizer.com),(DOMAIN-SUFFIX,js.monitor.azure.com),(DOMAIN-SUFFIX,learn.khanacademy.org),(DOMAIN-SUFFIX,link.meet5.net),(DOMAIN-SUFFIX,link.morningbrew.com),(DOMAIN-SUFFIX,link.sylikes.com),(DOMAIN-SUFFIX,linka.page),(DOMAIN-SUFFIX,links.e.theatlantic.com),(DOMAIN-SUFFIX,links.getblueshift.com),(DOMAIN-SUFFIX,local.adguard.org),(DOMAIN-SUFFIX,log.mmstat.com),(DOMAIN-SUFFIX,logentries.com),(DOMAIN-SUFFIX,login.gaijin.net),(DOMAIN-SUFFIX,login.sendpulse.com),(DOMAIN-SUFFIX,ma135-r.analytics.edgekey.net),(DOMAIN-SUFFIX,manwa.me),(DOMAIN-SUFFIX,marketing.net.idealo-partner.com),(DOMAIN-SUFFIX,media-consumer365.desigual.com),(DOMAIN-SUFFIX,my.tealiumiq.com),(DOMAIN-SUFFIX,netatmo.commander1.com),(DOMAIN-SUFFIX,news.warhammer.com),(DOMAIN-SUFFIX,nineto5mac-d.openx.net),(DOMAIN-SUFFIX,oa.tr.line.me),(DOMAIN-SUFFIX,obituaries.startribune.com),(DOMAIN-SUFFIX,obituaries.therecord.com),(DOMAIN-SUFFIX,obituaries.thestar.com),(DOMAIN-SUFFIX,obituaries.toacorn.com),(DOMAIN-SUFFIX,official.paymaya.com),(DOMAIN-SUFFIX,om-ssl.consorsbank.de),(DOMAIN-SUFFIX,omniture.walmart.com),(DOMAIN-SUFFIX,omsc.kpn.com),(DOMAIN-SUFFIX,oneline.nextday.media),(DOMAIN-SUFFIX,onl.bz),(DOMAIN-SUFFIX,pagead.l.doubleclick.net),(DOMAIN-SUFFIX,partner.everydays.de),(DOMAIN-SUFFIX,partner.o2online.de),(DOMAIN-SUFFIX,pgpartner.com),(DOMAIN-SUFFIX,pics.porn300.com),(DOMAIN-SUFFIX,prod.impartner.live),(DOMAIN-SUFFIX,promo.gramedia.com),(DOMAIN-SUFFIX,proto2ad.durasite.net),(DOMAIN-SUFFIX,pt.afl.rakuten.co.jp),(DOMAIN-SUFFIX,public-cis.exponea.com),(DOMAIN-SUFFIX,puma.112.2o7.net),(DOMAIN-SUFFIX,puzzles-games-api.gp-prod.conde.digital),(DOMAIN-SUFFIX,px.a8.net),(DOMAIN-SUFFIX,radiofrance.targetspot.com),(DOMAIN-SUFFIX,rd.bizrate.com),(DOMAIN-SUFFIX,recommender.scarabresearch.com),(DOMAIN-SUFFIX,redir.ownpage.fr),(DOMAIN-SUFFIX,redirect.appmetrica.yandex.com),(DOMAIN-SUFFIX,redirect.disqus.com),(DOMAIN-SUFFIX,ref.rbauction.com),(DOMAIN-SUFFIX,refer.discover.com),(DOMAIN-SUFFIX,remembering.ca),(DOMAIN-SUFFIX,reports.adguard.com),(DOMAIN-SUFFIX,res.ads.nicovideo.jp),(DOMAIN-SUFFIX,s.bluecore.com),(DOMAIN-SUFFIX,s.optnx.com),(DOMAIN-SUFFIX,s1.wp.com),(DOMAIN-SUFFIX,sax.sina.com.cn),(DOMAIN-SUFFIX,sbs.demdex.net),(DOMAIN-SUFFIX,secureimage.securedataimages.com),(DOMAIN-SUFFIX,sedge.nfl.com),(DOMAIN-SUFFIX,sgqcvfjvr.onet.pl),(DOMAIN-SUFFIX,smtp.focusgroupresearch.com),(DOMAIN-SUFFIX,sobot.com),(DOMAIN-SUFFIX,spartaindependent.com),(DOMAIN-SUFFIX,ssai.aniview.com),(DOMAIN-SUFFIX,stash.roistat.com),(DOMAIN-SUFFIX,stats.britishbaseball.org.uk),(DOMAIN-SUFFIX,str.hit.gemius.pl),(DOMAIN-SUFFIX,support-beacon.nakanohito.jp),(DOMAIN-SUFFIX,support-widget.nakanohito.jp),(DOMAIN-SUFFIX,surveymyopinion.researchnow.com),(DOMAIN-SUFFIX,swasc.homedepot.com),(DOMAIN-SUFFIX,tags.crwdcntrl.net),(DOMAIN-SUFFIX,taiga.maven.io),(DOMAIN-SUFFIX,tlh.gedidigital.it),(DOMAIN-SUFFIX,tms.capitalone.com),(DOMAIN-SUFFIX,torimochi.line-apps.com),(DOMAIN-SUFFIX,tr.rdrtr.com),(DOMAIN-SUFFIX,track.rutarget.ru),(DOMAIN-SUFFIX,track.webgains.com),(DOMAIN-SUFFIX,trk.ecomm.lenovo.com),(DOMAIN-SUFFIX,unsubscribe.email.premierleague.com),(DOMAIN-SUFFIX,unsubscribe.lhinsights.com),(DOMAIN-SUFFIX,used.ca),(DOMAIN-SUFFIX,validate.perfdrive.com),(DOMAIN-SUFFIX,vcentry2.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vcentry3.valuecommerce.ne.jp),(DOMAIN-SUFFIX,vitacost.122.2o7.net),(DOMAIN-SUFFIX,wan.douyu.com),(DOMAIN-SUFFIX,webstatic.nero.com),(DOMAIN-SUFFIX,www.datadoghq-browser-agent.com),(DOMAIN-SUFFIX,www.dogpile.com),(DOMAIN-SUFFIX,www.googleadservices.com),(DOMAIN-SUFFIX,www.jdoqocy.com),(DOMAIN-SUFFIX,www.statcounter.com),(DOMAIN-SUFFIX,wwwimage-tve.cbsstatic.com))))))`

### scope-78b0ee7a110526c9

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`DOMAIN-SUFFIX,canadiantire.ca.data.adobedc.net`

### scope-5d7e26c5a08918af

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`DOMAIN-SUFFIX,ss.handyhand.dk`

### scope-26083f42a39f8f23

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`DOMAIN-SUFFIX,triangle.com.data.adobedc.net`

### scope-c342922d0f506c1f

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`DOMAIN-SUFFIX,westpac.co.nz.data.adobedc.net`

### allow-change-clash_allow

Allow scope changed

### scope-18ab22b4b0b703f0

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`||canadiantire.ca.data.adobedc.net^`

### scope-148e3bf8fbba0b1f

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`||ss.handyhand.dk^`

### scope-2af1dcec0e314d17

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`||triangle.com.data.adobedc.net^`

### scope-d48f974f01964e78

Broader suffix replaced exact/subdomain

- 目标：unknown
- 规则：`||westpac.co.nz.data.adobedc.net^`

### allow-change-adguard_allow

Allow scope changed

### impact-a9185f2d4867f333

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-ad.sm.cn`
- 来源：awa-clash，sources/awa-clash.txt:1007
- gecko-service：`probe-ad.sm.cn.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.sm.cn.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.sm.cn.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-0082db7e5e882fb3

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-ad.video.yximgs.com`
- 来源：awa-clash，sources/awa-clash.txt:1008
- gecko-service：`probe-ad.video.yximgs.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.video.yximgs.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.video.yximgs.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-dbd8efd29647f375

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-ad.wtzw.com`
- 来源：awa-clash，sources/awa-clash.txt:1009
- gecko-service：`probe-ad.wtzw.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.wtzw.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.wtzw.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-b153447f90355ff4

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-be-pack-sign.pglstatp-toutiao.com`
- 来源：awa-clash，sources/awa-clash.txt:1010
- gecko-service：`probe-be-pack-sign.pglstatp-toutiao.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-be-pack-sign.pglstatp-toutiao.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-be-pack-sign.pglstatp-toutiao.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-5d5d95388b56e77a

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,111.20.26.186/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:13
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-d124d4898fd8e189

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,112.84.130.73/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:14
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-dfd3b325acb20d08

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,116.142.251.100/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:15
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-378df5d643363f35

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,116.177.251.215/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:16
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-0ccd30ef7d5ace26

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,120.77.173.114/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:17
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-212ab678a2830d83

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,123.56.23.22/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:18
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-6e875846585264aa

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,14.29.101.160/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:19
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-1b9db71a2b48199a

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,14.29.101.168/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:20
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-5e66fb371ad71cc3

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,14.29.101.169/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:21
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-1a79e533d8631f04

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,182.254.116.116/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:22
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-f56141b995daac45

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,203.205.137.89/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:23
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-a51869ec69d8467a

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,218.77.192.51/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:24
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-06589875c3f1fab0

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,38.190.225.166/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:25
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-4ced1257045e303a

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-ad.sm.cn*`
- 来源：awa-dns，sources/awa-dns.txt:993
- gecko-service：`probe-ad.sm.cn.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.sm.cn.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.sm.cn.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-7499d33337faa518

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-ad.video.yximgs.com*`
- 来源：awa-dns，sources/awa-dns.txt:994
- gecko-service：`probe-ad.video.yximgs.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.video.yximgs.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.video.yximgs.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-863c64916b43c713

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-ad.wtzw.com*`
- 来源：awa-dns，sources/awa-dns.txt:995
- gecko-service：`probe-ad.wtzw.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.wtzw.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.wtzw.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-078083ab522df9cb

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-be-pack-sign.pglstatp-toutiao.com*`
- 来源：awa-dns，sources/awa-dns.txt:996
- gecko-service：`probe-be-pack-sign.pglstatp-toutiao.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-be-pack-sign.pglstatp-toutiao.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-be-pack-sign.pglstatp-toutiao.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）


完整变更见 validation.json，处理与原文位置见 decisions.json、rules.jsonl.gz。
