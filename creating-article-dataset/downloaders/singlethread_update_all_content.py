#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:03:05 2020

@author: marco
"""

import pandas as pd
from newsparsers.fanpage_parser import FanpageParser #www.fanpage.it
from newsparsers.ilfattoquotidiano import IlFattoQuotidianoParser # www.ilfattoquotidiano.it
from newsparsers.blitz_quotidiano import BlitzParser # www.blitzquotidiano.it
from newsparsers.meridiano_news import IlMeridianoNewsParser #www.ilmeridianonews.it
from newsparsers.carabinieri import CarabinieriParser
from newsparsers.liberoquotidiano import LiberoQuotidianoParser
from newsparsers.ilgiornale import IlGiornaleParser
from newsparsers.tgcom import TgCom24Parser
from newsparsers.gazzetta_mezzogiorno import LaGazzettaDelMezzogiornoParser #www.lagazzettadelmezzogiorno.it
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
from newsparsers.campanianotizie import CampaniaNotizieParser
from newsparsers.viveremarche import VivereMarcheParser
from newsparsers.corriereadriatico import CorriereAdriaticoParser
from newsparsers.marchenotizie import MarcheNotizieParser
from newsparsers.tmnotizie import TMNotizieParser
from newsparsers.ilmessaggero import IlMessaggeroParser
from newsparsers.cronacaqui import CronacaQuiParser
from newsparsers.nuovasardegna import LaNuovaSardegnaParser
from newsparsers.aostanews import AostaNewsParser
from newsparsers.molisenetwork import MoliseNetworkParser
from newsparsers.toscananews import ToscanaNewsParser
from newsparsers.basilicatanews24 import BasilicataNews24Parser
from newsparsers.umbriajournal import UmbriaJournalParser
from newsparsers.cnaemiliaromagna import CNAEmiliaRomagnaParser
from newsparsers.ilfriuli import IlFriuliParser
from newsparsers.ildolomiti import IlDolomitiParser
from newsparsers.abruzzonews import AbruzzoNewsParser

#articles_dataset_path = '/home/marco/workspace/git/StatLearnTeam/dataset/articles_dataset.csv'
#articles_dataset_path = '/home/marco/workspace/git/StatLearnTeam/dataset/nuova_sardegna.csv'

articles_dataset_path_root = '/home/marco/workspace/git/StatLearnTeam/dataset/'
updated_datasets_root_path = '/home/marco/workspace/git/StatLearnTeam/dataset/updated_contents/'

#dataset = pd.read_csv(articles_dataset_path, sep = ';', index_col = 0)

#p = MoliseNetworkParser('www.molisenetwork.net', dataset_path = articles_dataset_path_root + 'molisenetwork.csv')
#p = ToscanaNewsParser('www.toscana-notizie.it', dataset_path = articles_dataset_path_root + 'toscananotizie.csv')
#p = BasilicataNews24Parser('www.basilicata24.it', dataset_path = articles_dataset_path_root + 'basilicatanews24.csv')
#p = UmbriaJournalParser('www.umbriajournal.com', dataset_path = articles_dataset_path_root + 'umbriajournal.csv')


#p = CNAEmiliaRomagnaParser('www.cnaemiliaromagna.it', dataset_path = articles_dataset_path_root + 'cnaemiliaromagna.csv')
#p = IlFriuliParser('www.ilfriuli.it', dataset_path = articles_dataset_path_root + 'ilfriuli.csv')
#p = IlDolomitiParser('www.ildolomiti.it', dataset_path = articles_dataset_path_root + 'ildolomiti.csv')


#p = AbruzzoNewsParser('www.abruzzonews.eu', dataset_path = articles_dataset_path_root + 'abruzzonews.csv')
p = LaNuovaSardegnaParser('www.lanuovasardegna.it', dataset_path = articles_dataset_path_root + 'lanuovasardegna.csv')
p.get_updated_dataset()
p.write_dataset_to_file(updated_datasets_root_path)

pdataset = p.dataset