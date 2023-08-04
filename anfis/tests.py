import sys

import anfis
import membership.mfDerivs
import membership.membershipfunction
import numpy

# ts = numpy.loadtxt("trainingSet.txt", usecols=[1, 2, 3])
ts = numpy.loadtxt("BMI_training_set.txt", usecols=[1, 2, 3, 4])
# numpy.loadtxt('c:\\Python_fiddling\\myProject\\MF\\trainingSet.txt',usecols=[1,2,3])
X = ts[:, 0:3]
Y = ts[:, 3]

# print ("X: "+str(X))
# print ("Y: "+str(Y))

# Percobaan
for value in X:
    print ("nilai" + str(value[0]))

# ini untuk menentukan Kurva fuzzy gaussian
# penjelasan: https://www.youtube.com/watch?v=vG6aZEgbAVU
# umur_1 = numpy.linspace(0, 15, 16)  # 0-15 umur_muda
# umur_2 = numpy.linspace(16, 30, 15)  # 16-30 umur dewasa muda
# umur_3 = numpy.linspace(31, 50, 15)  # 31-50 umur dewasa lanjut
# umur_4 = numpy.linspace(51, 100, 15)  # 50-100 umur lansia

umur_1 = numpy.linspace(0, 15, 16)  # 0-15 umur_muda
umur_2 = numpy.linspace(13, 30, 18)  # 16-30 umur dewasa muda
umur_3 = numpy.linspace(28, 50, 18)  # 31-50 umur dewasa lanjut
umur_4 = numpy.linspace(58, 100, 18)  # 50-100 umur lansia


umur = []
umur.append(umur_1)
umur.append(umur_2)
umur.append(umur_3)
umur.append(umur_4)

# tinggi_1 = numpy.linspace(0, 50, 51)  # 0-50 pendek
# tinggi_2 = numpy.linspace(51, 100, 50)  # 51-100 pendek mengengah
# tinggi_3 = numpy.linspace(101, 150, 50)  # 101-150 menengah
# tinggi_4 = numpy.linspace(151, 200, 50)  # 151-200 tinggi

tinggi_1 = numpy.linspace(0, 50, 51)  # 0-50 pendek
tinggi_2 = numpy.linspace(48, 100, 53)  # 51-100 pendek mengengah
tinggi_3 = numpy.linspace(98, 150, 53)  # 101-150 menengah
tinggi_4 = numpy.linspace(148, 200, 53)  # 151-200 tinggi


tinggi = []
tinggi.append(tinggi_1)
tinggi.append(tinggi_2)
tinggi.append(tinggi_3)
tinggi.append(tinggi_4)

# berat_1 = numpy.linspace(0, 50, 51)  # 0-50 lanjutin sendiri wkkw
# berat_2 = numpy.linspace(51, 100, 50)  # 51-100
# berat_3 = numpy.linspace(101, 150, 50)  # 101-150
# berat_4 = numpy.linspace(151, 200, 50)  # 151-200

berat_1 = numpy.linspace(0, 50, 51)  # 0-50 lanjutin sendiri wkkw
berat_2 = numpy.linspace(48, 100, 53)  # 51-100
berat_3 = numpy.linspace(198, 150, 53)  # 101-150
berat_4 = numpy.linspace(148, 200, 53)  # 151-200

berat = []
berat.append(berat_1)
berat.append(berat_2)
berat.append(berat_3)
berat.append(berat_4)

umur_mean_sigma = []
tinggi_mean_sigma = []
berat_mean_sigma = []

mf = []

# menghitung mean dan sigma tiap array
for item in umur:
    sigma = round(numpy.std(item), 1)
    mean = round(numpy.mean(item), 1)
    umur_mean_sigma.append(
        ['gaussmf', {'mean': mean, 'sigma': sigma}]
    )
mf.append(umur_mean_sigma)
    # print (str(item))
    # print ("mean: " + str(mean))
    # print ("sigma: " + str(round(sigma, 2)))
for item in tinggi:
    sigma = round(numpy.std(item), 1)
    mean = round(numpy.mean(item), 1)
    tinggi_mean_sigma.append(
        ['gaussmf', {'mean': mean, 'sigma': sigma}]
    )
mf.append(tinggi_mean_sigma)

for item in berat:
    sigma = round(numpy.std(item), 1)
    mean = round(numpy.mean(item), 1)
    berat_mean_sigma.append(
        ['gaussmf', {'mean': mean, 'sigma': sigma}]
    )
mf.append(berat_mean_sigma)

# print (str(mf))
# sigma = numpy.std(X[:,0])
# mean =  numpy.mean(X[:,0])
# print(X[:,0])
# print (umur_2)
# print (sigma)
# print (mean)
# sys.exit()

# mf = [
#     [
#         ['gaussmf', {'mean': 0., 'sigma': 1.}],
#         ['gaussmf', {'mean': -1., 'sigma': 2.}],
#         ['gaussmf', {'mean': -4., 'sigma': 10.}],
#         ['gaussmf', {'mean': -7., 'sigma': 7.}]
#     ],
#     [
#         ['gaussmf', {'mean': 1., 'sigma': 2.}],
#         ['gaussmf', {'mean': 2., 'sigma': 3.}],
#         ['gaussmf', {'mean': -2., 'sigma': 10.}],
#         ['gaussmf', {'mean': -10.5, 'sigma': 5.}]
#     ],
#     [
#         ['gaussmf', {'mean': 1., 'sigma': 2.}],
#         ['gaussmf', {'mean': 2., 'sigma': 3.}],
#         ['gaussmf', {'mean': -2., 'sigma': 10.}],
#         ['gaussmf', {'mean': -10.5, 'sigma': 5.}]
#     ],
# ]

mf2 = [
    [
        ['gaussmf', {'mean': 9.26, 'sigma': 1}],
        ['gaussmf', {'mean': 9.26, 'sigma': 33.33}],
        ['gaussmf', {'mean': 9.26, 'sigma': 66.67}],
        ['gaussmf', {'mean': 9.26, 'sigma': 100}]
    ],
    [
        ['gaussmf', {'mean': 35.38, 'sigma': 1}],
        ['gaussmf', {'mean': 35.38, 'sigma': 100}],
        ['gaussmf', {'mean': 35.38, 'sigma': 200}]
    ],
    [
        ['gaussmf', {'mean': 35.39, 'sigma': 1}],
        ['gaussmf', {'mean': 35.38, 'sigma': 100}],
        ['gaussmf', {'mean': 35.37, 'sigma': 200}]
    ],
]

mfc = membership.membershipfunction.MemFuncs(mf2)
anf = anfis.ANFIS(X, Y, mfc)
anf.trainHybridJangOffLine(epochs=20)
print(round(anf.consequents[-1][0], 6))
print(round(anf.consequents[-2][0], 6))
print(round(anf.fittedValues[9][0], 6))
if round(anf.consequents[-1][0], 6) == -5.275538 and round(anf.consequents[-2][0], 6) == -1.990703 and round(
        anf.fittedValues[9][0], 6) == 0.002249:
    print('test is good')

print("Plotting errors")
anf.plotErrors()
print("Plotting results")
anf.plotResults()

print ("mean count:" + str(membership.mfDerivs.global_mean_count))
print ("sigma count:" + str(membership.mfDerivs.global_sigma_count))
