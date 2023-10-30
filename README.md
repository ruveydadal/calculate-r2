# r2-hesaplama
Machine Learning-4

Bu örnek, makine öğrenimi ile regresyon analizini uygulamak için kullanılan Python kodunu içerir. Özellikle, doğrusal regresyon, polinom regresyon ve rastgele orman regresyon algoritmalarını kullanarak maaş verileri üzerinde bir analiz yapar.

## Kullanılan Teknolojiler
- Python 3.x
- NumPy
- Matplotlib
- pandas
- scikit-learn (sklearn)

## Veri Kaynağı
Bu kod örneği, 'maaslar.csv' adlı bir CSV dosyasından verileri okur. Veri dosyasının her satırı bir kişinin deneyim yılına ve maaşına karşılık gelir.

## Kod Açıklaması
Bu kod örneği aşağıdaki başlıklar altında çalışmaktadır:

* Verilerin okunması: 'maaslar.csv' dosyası okunur ve veriler x (deneyim yılı) ve y (maaş) olarak ayrılır.

* Doğrusal Regresyon: sklearn.linear_model kullanılarak doğrusal regresyon uygulanır ve sonuçlar grafiğe çizilir.

* Polinom Regresyon: İki farklı derecede (2. derece ve 4. derece) polinom regresyon uygulanır ve sonuçlar ilgili grafiklerde gösterilir.

* Rastgele Orman Regresyon: sklearn.ensemble kullanılarak rastgele orman regresyonu uygulanır ve sonuçlar grafiğe çizilir.

* R^2 Değerleri: Her regresyon yöntemi için R-kare (R^2) değerleri hesaplanır ve yazdırılır.

## Örnek Çıktılar
Kod çalıştırıldığında, her bir regresyon yönteminin sonuçları grafiğe çizilir. Ayrıca, R^2 değerleri de yazdırılır.
