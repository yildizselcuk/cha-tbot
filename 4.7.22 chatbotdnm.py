# pip#install nltk
from nltk.chat.util import Chat, reflections

soru_cevaplar = [
    ["Merhaba", ["Merhaba ben Gaffur, sizin adınız neydi?"]],
    ["Benim adım (.*)", ["Çok memnun oldum %1"]],
    ["Kaç yaşındasınız Gaffur bey", ["Yapay zeka olduğum için herhangibir cinsiyete sahip ddeğilim, belli bir yaşım da "
                                     "yok ama 2022 de yazıldım."]],
    ["Benim bir (.*) sitem var",
     ["%1 siteleri güzeldir.", "%1 siteleri yararlıdır.", "%1 siteni geliştirmede yardım ister misin?"]],

]
chat = Chat(soru_cevaplar, reflections)
chat.converse(quit="bitti")
