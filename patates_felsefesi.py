#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PATATES FELSEFESİ ÜRETECİ v1.0
Evrenin en derin sırlarını patates üzerinden çözmek için tasarlanmış
bilimsel ve kesinlikle gerekli bir araç.
"""

import random
import time

PATATES_SOZLER = [
    "Patates, toprağın altında düşünür. Sen ise yüzeyde kaybolmuşsun.",
    "Bir patatesin gözleri vardır ama görmez. Senin gözlerin var ama bakmazsın.",
    "Haşlanmış patates gibi yumuşak ol, ama kızarmış gibi diren.",
    "Patatesin ruhu, yağda kızarırken özgürlüğe kavuşur.",
    "Neden patates? Çünkü evrenin cevabı her zaman 'patates'tir.",
    "Bir patatese bakıp 'ben de bir patatesim' demek, aydınlanmanın ilk adımıdır.",
    "Patates büyür, sen küçülürsün. Bu adaletsizliktir.",
    "Kızarmış patatesin çıtır sesi, varoluşun en samimi itirafıdır.",
    "Patatesin içinde yıldızlar gizlidir. Kes onu, göreceksin.",
    "Sen bir insan mısın yoksa henüz pişmemiş bir patates mi?",
    "Patates hiçbir şey sormaz. Bu yüzden her şeyi bilir.",
    "Hayat kısa, patates uzundur. (Bazen.)",
    "Bir patatesin kaderi tencereye düşmektir. Senin kaderin de benzer.",
    "Patates felsefesi: Ne kadar derine inerse o kadar bilge olur.",
    "Bugün bir patates yedin mi? Yoksa patates mi seni yedi?",
]

def dramatik_yukle():
    print("Patates ruhu çağrılıyor...")
    time.sleep(1.2)
    print("Toprak katmanları açılıyor...")
    time.sleep(0.8)
    print("Derinliklerden felsefe yükseliyor...")
    time.sleep(1.0)
    print()

def uret():
    dramatik_yukle()
    soz = random.choice(PATATES_SOZLER)
    print("=" * 60)
    print("  PATATES FELSEFESİ v1.0 - EVRENİN GERÇEK CEVABI")
    print("=" * 60)
    print()
    print(f"  >>> {soz}")
    print()
    print("=" * 60)
    print("Bu sözü bir yere not et. Hayatın değişebilir.")
    print("veya değişmez. Patates karar verir.")
    print("=" * 60)

if __name__ == "__main__":
    uret()
