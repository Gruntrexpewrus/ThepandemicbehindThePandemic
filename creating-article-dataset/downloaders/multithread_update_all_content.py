#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:28:20 2020

@author: marco
"""



import threading
from newsparsers.fanpage_parser import FanpageParser
from newsparsers.ilfattoquotidiano import IlFattoQuotidianoParser
from newsparsers.blitz_quotidiano import BlitzParser
from newsparsers.meridiano_news import IlMeridianoNewsParser
from newsparsers.carabinieri import CarabinieriParser
from newsparsers.liberoquotidiano import LiberoQuotidianoParser
from newsparsers.ilgiornale import IlGiornaleParser
from newsparsers.tgcom import TgCom24Parser
from newsparsers.gazzetta_mezzogiorno import LaGazzettaDelMezzogiornoParser
from newsparsers.strettoweb import StrettoWebParser # www.strettoweb.com
from newsparsers.salernonotizie import SalernonotizieParser # www.salernonotizie.it
from newsparsers.meteoweb import MeteowebParser # www.meteoweb.eu
from newsparsers.lastampa import LaStampaParser
from newsparsers.lecodelchisone import LEcoDelChisoneParser
from newsparsers.gazzettadellosport import LaGazzettaDelloSportParser
from newsparsers.telegranducato import TeleGranDucatoDiToscanaParser
from newsparsers.trmtv import TrmtvParser
from newsparsers.cronacaonline import CronacaOnlineParser
from newsparsers.ilmartino import IlMartinoParser
from newsparsers.laquilablog import LAquilaBlogParser
from newsparsers.ilgazzettinoweb import IlGazzettinoWebParser
from newsparsers.vvox import VvoxParser
from newsparsers.calabriapage import CalabriaPageParser
from newsparsers.ilcrotonese import IlCrotoneseParser
from newsparsers.calcioweb import CalcioWebParser
from newsparsers.ragusaoggi import RagusaOggiParser
from newsparsers.ligurianotizie import LiguriaNotizieParser
from newsparsers.ilsecoloxix import IlSecoloXIXParser
from newsparsers.ilsussidiario import IlSussidiarioParser
from newsparsers.asipress import AsiPressParser
from newsparsers.larepubblica import LaRepubblicaParser

class ThreadedParser(threading.Thread):
    def __init__(self, parser, save_path_root):
        threading.Thread.__init__(self)
        self.parser = parser
        self.save_path_root = save_path_root
    
    def run(self):
        print('Starting thread for ', str(type(self.parser)))
        self.parser.get_updated_dataset()
        self.parser.write_dataset_to_file(self.save_path_root)
        print('Thread for ', str(type(self.parser)), ' has finished')


articles_dataset_path = '/home/marco/workspace/git/StatLearnTeam/dataset/articles_dataset.csv'
updated_datasets_root_path = '/home/marco/workspace/git/StatLearnTeam/dataset/updated_contents/'
'''
t1 = ThreadedParser(FanpageParser('www.fanpage.it', articles_dataset_path), updated_datasets_root_path)
t2 = ThreadedParser(IlFattoQuotidianoParser('www.ilfattoquotidiano.it', articles_dataset_path), updated_datasets_root_path)
t3 = ThreadedParser(BlitzParser('www.blitzquotidiano.it', articles_dataset_path), updated_datasets_root_path)
t4 = ThreadedParser(IlMeridianoNewsParser('www.ilmeridianonews.it', articles_dataset_path), updated_datasets_root_path)
t5 = ThreadedParser(CarabinieriParser('www.carabinieri.it', articles_dataset_path), updated_datasets_root_path)

t6 = ThreadedParser(LiberoQuotidianoParser('www.liberoquotidiano.it', articles_dataset_path), updated_datasets_root_path)
t7 = ThreadedParser(IlGiornaleParser('www.ilgiornale.it', articles_dataset_path), updated_datasets_root_path)
t8 = ThreadedParser(TgCom24Parser('www.tgcom24.mediaset.it', dataset_path = articles_dataset_path), updated_datasets_root_path)
t9 = ThreadedParser(LaGazzettaDelMezzogiornoParser('www.lagazzettadelmezzogiorno.it', articles_dataset_path), updated_datasets_root_path)
t10 = ThreadedParser(StrettoWebParser('www.strettoweb.com', articles_dataset_path), updated_datasets_root_path)


t11 = ThreadedParser(SalernonotizieParser('www.salernonotizie.it', articles_dataset_path), updated_datasets_root_path)
t12 = ThreadedParser(MeteowebParser('www.meteoweb.eu', articles_dataset_path), updated_datasets_root_path)
t13 = ThreadedParser(LaStampaParser('www.lastampa.it', articles_dataset_path), updated_datasets_root_path)
t14 = ThreadedParser(LEcoDelChisoneParser('www.ecodelchisone.it', articles_dataset_path), updated_datasets_root_path)
t15 = ThreadedParser(LaGazzettaDelloSportParser('www.gazzetta.it', articles_dataset_path), updated_datasets_root_path)

t16 = ThreadedParser(TeleGranDucatoDiToscanaParser('www.telegranducato.it', articles_dataset_path), updated_datasets_root_path)
t17 = ThreadedParser(TrmtvParser('www.trmtv.it', articles_dataset_path), updated_datasets_root_path)
t18 = ThreadedParser(CronacaOnlineParser('www.cronacaonline.it', articles_dataset_path), updated_datasets_root_path)
t19 = ThreadedParser(IlMartinoParser('www.ilmartino.it', articles_dataset_path), updated_datasets_root_path)
t20 = ThreadedParser(LAquilaBlogParser('www.laquilablog.it', articles_dataset_path), updated_datasets_root_path)


t16 = ThreadedParser(IlGazzettinoWebParser('www.ilgazzettino.it', articles_dataset_path), updated_datasets_root_path)
t17 = ThreadedParser(VvoxParser('www.vvox.it', articles_dataset_path), updated_datasets_root_path)
t18 = ThreadedParser(CalabriaPageParser('www.calabriapage.it', articles_dataset_path), updated_datasets_root_path)
t19 = ThreadedParser(IlCrotoneseParser('www.ilcrotonese.it', articles_dataset_path), updated_datasets_root_path)
t20 = ThreadedParser(CalcioWebParser('www.calcioweb.eu', articles_dataset_path), updated_datasets_root_path)

t21 = ThreadedParser(RagusaOggiParser('www.ragusaoggi.it', articles_dataset_path), updated_datasets_root_path)
t22 = ThreadedParser(LiguriaNotizieParser('www.ligurianotizie.it', articles_dataset_path), updated_datasets_root_path)
t23 = ThreadedParser(IlSecoloXIXParser('www.ilsecoloxix.it', articles_dataset_path), updated_datasets_root_path)
t24 = ThreadedParser(IlSussidiarioParser('www.ilsussidiario.net', articles_dataset_path), updated_datasets_root_path)
t25 = ThreadedParser(AsiPressParser('www.asipress.it', articles_dataset_path), updated_datasets_root_path)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t20.start()
t21.start()
t22.start()
t23.start()
t24.start()
t25.start()

# FANPAGE
t1.join()

t26 = ThreadedParser(FanpageParser('napoli.fanpage.it', articles_dataset_path), updated_datasets_root_path)
t29 = ThreadedParser(LaRepubblicaParser('www.repubblica.it', articles_dataset_path), updated_datasets_root_path)
t26.start()
t29.start()
t26.join()
t29.join()


t27 = ThreadedParser(FanpageParser('milano.fanpage.it', articles_dataset_path), updated_datasets_root_path)
t30 = ThreadedParser(LaRepubblicaParser('bari.repubblica.it', articles_dataset_path), updated_datasets_root_path)
t27.start()
t30.start()
t27.join()
t30.join()

t28 = ThreadedParser(FanpageParser('roma.fanpage.it', articles_dataset_path), updated_datasets_root_path)
t31 = ThreadedParser(LaRepubblicaParser('bologna.repubblica.it', articles_dataset_path), updated_datasets_root_path)
t28.start()
t31.start()


from newsparsers.campanianotizie import CampaniaNotizieParser
from newsparsers.viveremarche import VivereMarcheParser
from newsparsers.corriereadriatico import CorriereAdriaticoParser
from newsparsers.marchenotizie import MarcheNotizieParser
from newsparsers.tmnotizie import TMNotizieParser
from newsparsers.ilmessaggero import IlMessaggeroParser
from newsparsers.cronacaqui import CronacaQuiParser



marchenotizie_websites = ['www.pesarourbinonotizie.it',
 'www.anconanotizie.it',
 'www.ascolinotizie.it',
 'www.maceratanotizie.it',
 'www.fermonotizie.info']

t32 = ThreadedParser(CampaniaNotizieParser('www.campanianotizie.com', articles_dataset_path), updated_datasets_root_path)
t33 = ThreadedParser(VivereMarcheParser('www.viveremarche.it', articles_dataset_path), updated_datasets_root_path)
t34 = ThreadedParser(CorriereAdriaticoParser('www.corriereadriatico.it', articles_dataset_path), updated_datasets_root_path)

t35 = ThreadedParser(MarcheNotizieParser(marchenotizie_websites[0], articles_dataset_path), updated_datasets_root_path)
t36 = ThreadedParser(MarcheNotizieParser(marchenotizie_websites[1], articles_dataset_path), updated_datasets_root_path)
t37 = ThreadedParser(MarcheNotizieParser(marchenotizie_websites[2], articles_dataset_path), updated_datasets_root_path)
t38 = ThreadedParser(MarcheNotizieParser(marchenotizie_websites[3], articles_dataset_path), updated_datasets_root_path)
t39 = ThreadedParser(MarcheNotizieParser(marchenotizie_websites[4], articles_dataset_path), updated_datasets_root_path)

t40 = ThreadedParser(IlMessaggeroParser('www.ilmessaggero.it', articles_dataset_path), updated_datasets_root_path)
t41 = ThreadedParser(CronacaQuiParser('www.cronacaqui', articles_dataset_path), updated_datasets_root_path)
t42 = ThreadedParser(TMNotizieParser('www.tmnotizie', articles_dataset_path), updated_datasets_root_path)


t32.start()
t33.start()
t34.start()
t35.start()
t36.start()
t37.start()
t38.start()
t39.start()
t40.start()
t41.start()
t42.start()

'''


from newsparsers.molisenetwork import MoliseNetworkParser
from newsparsers.toscananews import ToscanaNewsParser
from newsparsers.basilicatanews24 import BasilicataNews24Parser
from newsparsers.umbriajournal import UmbriaJournalParser
from newsparsers.cnaemiliaromagna import CNAEmiliaRomagnaParser
from newsparsers.ilfriuli import IlFriuliParser
from newsparsers.ildolomiti import IlDolomitiParser

articles_dataset_path_root = '/home/marco/workspace/git/StatLearnTeam/dataset/'

t43 = ThreadedParser(MoliseNetworkParser('www.molisenetwork.net', dataset_path = articles_dataset_path_root + 'molisenetwork.csv'), updated_datasets_root_path)
t44 = ThreadedParser(ToscanaNewsParser('www.toscana-notizie.it', dataset_path = articles_dataset_path_root + 'toscananotizie.csv'), updated_datasets_root_path)
t45 = ThreadedParser(BasilicataNews24Parser('www.basilicata24.it', dataset_path = articles_dataset_path_root + 'basilicatanews24.csv'), updated_datasets_root_path)
t46 = ThreadedParser(UmbriaJournalParser('www.umbriajournal.com', dataset_path = articles_dataset_path_root + 'umbriajournal.csv'), updated_datasets_root_path)
t47 = ThreadedParser(CNAEmiliaRomagnaParser('www.cnaemiliaromagna.it', dataset_path = articles_dataset_path_root + 'cnaemiliaromagna.csv'), updated_datasets_root_path)
t48 = ThreadedParser(IlFriuliParser('www.ilfriuli.it', dataset_path = articles_dataset_path_root + 'ilfriuli.csv'), updated_datasets_root_path)
t49 = ThreadedParser(IlDolomitiParser('www.ildolomiti.it', dataset_path = articles_dataset_path_root + 'ildolomiti.csv'), updated_datasets_root_path)

t43.start()
t44.start()
t45.start()
t46.start()
t47.start()
t48.start()
t49.start()
















