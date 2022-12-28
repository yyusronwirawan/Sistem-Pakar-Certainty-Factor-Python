penyakit = ["Anemia", "Bronkhitis", "Flu", "Demam"]
gejala = ["Badan Panas", "Sakit Kepala", "Bersin-Bersin", "Batuk", "Pilek, Hidung Buntu", \
    "Badan Lemas", "Kedinginan"]

pengetahuan = [
    ["Anemia", "Sakit Kepala", 0.7, 0.2],
    ["Anemia", "Badan Lemas", 0.8, 0.1],
    ["Bronkhitis", "Badan Panas", 0.6, 0.2],
    ["Bronkhitis", "Bersin-Bersin", 0.7, 0.4],
    ["Bronkhitis", "Batuk", 0.8, 0.1],
    ["Demam", "Kedinginan", 0.7, 0.1],
    ["Demam", "Badan Lemas", 0.6, 0.2],
    ["Demam", "Badan Panas", 0.8, 0.1],
    ["Flu", "Badan Panas", 0.6, 0.2],
    ["Flu", "Sakit Kepala", 0.7, 0.2],
    ["Flu", "Bersin-Bersin", 0.6, 0.2],
    ["Flu", "Pilek, Hidung Buntu", 0.8, 0.1],
    ["Flu", "Badan Lemas", 0.7, 0.1],
    ["Flu", "Kedinginan", 0.8, 0.5]
]
gejala_dipilih = []
for i in range(len(gejala)):
    jawab = input("Apakah Mengalami "+gejala[i]+"(Y/T?")
    if jawab.upper() == "Y":
        gejala_dipilih.append(gejala[i])
print("Gejala Dipilih",gejala_dipilih)
penyakit_terpilih = []
for i in range(len(pengetahuan)):
    for j in range(len(gejala_dipilih)):
        if (pengetahuan[i][1] == gejala_dipilih[j]):
            if pengetahuan[i][0] not in penyakit_terpilih:
                penyakit_terpilih.append(pengetahuan[i][0])
print("Penyakit Terpilih", penyakit_terpilih)
list_cf = []
for i in range(len(penyakit_terpilih)):
    print("===="+penyakit_terpilih[i]+"====")
    jmlpengetahuan = 0
    pengetahuanke = 0
    for j in range(len(pengetahuan)):
        if (pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
            jmlpengetahuan = jmlpengetahuan + 1
    mblama = 0
    mdlama = 0
    for j in range(len(pengetahuan)):
        if (pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
            pengetahuanke = pengetahuanke + 1
            if (jmlpengetahuan == 1):
                mb = pengetahuan[j][2]
                md = pengetahuan[j][3]
                cf = mb - md
                print("mb = ", mb)
                print("md = ", md)
                print("cf = mb - md = ", mb, " - ", md, " = ", cf);
                list_cf.append(cf)
            elif (jmlpengetahuan > 1):
                if (pengetahuanke == 1):
                    mblama = pengetahuan[j][2]
                    mdlama = pengetahuan[j][3]
                    print("mblama = ", mblama)
                    print("mdlama = ", mdlama)
                elif (pengetahuanke == 2):
                    mbbaru = pengetahuan[j][2]
                    mdbaru = pengetahuan[j][3]
                    mbsementara = (mblama + mbbaru) * (1 - mblama)
                    mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                    print("mbsementara = (mblama + mbbaru) * (1 - mblama) = (", \
                          mblama, " + ", mbbaru, ") * (1 - ", mblama, ") = ", mbsementara)
                    print("mdsementara = (mdlama + mdbaru) * (1 - mdlama) = (", \
                          mdlama, " + ", mdbaru, ") * (1 - ", mdlama, ") = ", mdsementara)
                    if (jmlpengetahuan == 2):
                        mb = mbsementara
                        md = mdsementara
                        cf = mb - md
                        print("mb = mbsementara = ", mb)
                        print("md = mdsementara = ", md)
                        print("cf = mb - md = ", mb, " - ", md, " = ", cf)
                        list_cf.append(cf)
                elif (pengetahuanke >= 3):
                    mblama = mbsementara
                    mdlama = mdsementara
                    print("mblama = mbsementara = ", mblama)
                    print("mdlama = mdsementara = ", mdlama)
                    mbbaru = pengetahuan[j][2]
                    mdbaru = pengetahuan[j][3]
                    print("mbbaru = ", mbbaru)
                    print("mdbaru = ", mdbaru)
                    mbsementara = (mblama + mbbaru) * (1 - mblama)
                    mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                    print("mbsementara = (mblama + mbbaru) * (1 - mblama) = (", \
                           mblama, " + ", mbbaru, ") * (1 - ", mblama, ") = ", mbsementara)
                    print("mdsementara = (mdlama + mdbaru) * (1 - mdlama) = (", \
                           mdlama, " + ", mdbaru, ") * (1 - ", mdlama, ") = ", mdsementara)
                    if (jmlpengetahuan == pengetahuanke):
                        mb = mbsementara
                        md = mdsementara
                        cf = mb - md
                        print("mb = mbsementara = ", mb)
                        print("md = mdsementara = ", md)
                        print("cf = mb - md = ", mb, " - ", md, " - ", cf)
                        list_cf.append(cf)
print("Penyakit Terpilih", penyakit_terpilih)
print(list_cf); stop=input("")
print(list_cf)
penyakitrangking = []
cfrangking = []
for i in range(len(penyakit_terpilih)):
    penyakitrangking.append(penyakit_terpilih[i])
    cfrangking.append(list_cf[i])
for i in range(len(penyakit_terpilih)):
    for j in range(len(penyakit_terpilih)):
        if j > i:
            if cfrangking[j] > cfrangking[i]:
                tmpcf = cfrangking[i]
                tmppenyakit = penyakitrangking[i]
                cfrangking[i] = cfrangking[j]
                penyakitrangking[i] = penyakitrangking[j]
                cfrangking[j] = tmpcf
                penyakitrangking[j] = tmppenyakit
print("Rangking Penyakit:",penyakitrangking)
print("Rangking CF:", cfrangking)