# DefectVision AI

DefectVision AI, endüstriyel ürünlerdeki kusurları görüntü işleme ve yapay zekâ yöntemleriyle tespit etmeyi hedefleyen uçtan uca bir yazılım projesidir.

Proje; üretim partilerinin yönetimi, kusur tespiti, sonuçların izlenmesi ve raporlanması için web tabanlı bir platform olarak geliştirilecektir.

## Proje Durumu

Proje aktif geliştirme aşamasındadır.

Şu anda temel repository yapısı, geliştirme standartları ve dokümantasyon altyapısı kurulmaktadır.

## Planlanan Teknolojiler

- Backend: FastAPI ve Python
- Frontend: React, TypeScript ve Vite
- Veritabanı: PostgreSQL
- Makine Öğrenmesi: Python tabanlı görüntü işleme ve kusur tespit modelleri
- Altyapı: Docker ve Docker Compose
- Kalite Süreçleri: Testler, lint kontrolleri ve GitHub Actions CI

## Klasör Yapısı

- `backend/`: API ve backend uygulama kodları
- `frontend/`: Web kullanıcı arayüzü
- `ml/`: Görüntü işleme ve makine öğrenmesi bileşenleri
- `infrastructure/`: Docker ve altyapı yapılandırmaları
- `docs/`: Teknik dokümantasyon
- `scripts/`: Yardımcı geliştirme ve bakım scriptleri
- `tests/`: Proje testleri

## Geliştirme Süreci

Her geliştirme görevi ayrı bir GitHub Issue üzerinden, ilgili branch üzerinde yapılır. Değişiklikler doğrudan `main` branch'ine gönderilmez; pull request üzerinden incelenip birleştirilir.