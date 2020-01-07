# Particle-Swarm-Optimization

for her parçacık için
  parçacığı başlangıç konumuna getir
end
for her parçacık için 
  uygunluk değerini hesapla
   if uygunluk değeri pbest’den daya iyi ise
    şimdiki değeri yeni pbest olarak ayarla
end
tüm parçacıkların bulduğu pbest değerlerinin en iyisini, tüm parçacıkların gbest’i olarak ayarla
 for her parçacık için
  denklem(1)’e göre parçacık hızını hesapla
  denklem(2)’ye göre parçacık konumunu güncelle
 end
for maksimum iterasyon sayısına veya minimum hata koşulunu sağlanana kadar devam et
