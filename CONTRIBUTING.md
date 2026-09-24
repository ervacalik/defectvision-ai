# Katkı Rehberi

DefectVision AI projesine yapılacak tüm geliştirmeler, düzenli ve izlenebilir bir çalışma akışıyla yürütülmelidir.

## Genel Kurallar

* Her çalışma başlamadan önce ilgili bir GitHub Issue bulunmalıdır.
* Her Issue için ayrı bir branch oluşturulmalıdır.
* Değişiklikler doğrudan `main` branch'ine gönderilmemelidir.
* Çalışma tamamlandığında pull request açılarak `main` branch'ine birleştirilmelidir.
* Commit mesajları kısa, açıklayıcı ve İngilizce yazılmalıdır.

## Branch Kuralları

Branch isimleri aşağıdaki formatlardan biriyle oluşturulmalıdır:

```text
feature/<issue-no>-kisa-aciklama
fix/<issue-no>-kisa-aciklama
chore/<issue-no>-kisa-aciklama
docs/<issue-no>-kisa-aciklama
```

Örnekler:

```text
chore/1-monorepo-structure
feature/12-product-management
fix/25-invalid-image-upload
docs/3-update-readme
```

## Commit Kuralları

Commit mesajları aşağıdaki yapıdan birini kullanmalıdır:

```text
feat: kısa açıklama
fix: kısa açıklama
docs: kısa açıklama
test: kısa açıklama
chore: kısa açıklama
refactor: kısa açıklama
```

Örnekler:

```text
chore: create monorepo directory structure
docs: add contribution guidelines
feat: add product creation endpoint
fix: handle invalid image uploads
test: add product service tests
```

## Pull Request Kuralları

* Pull request ilgili Issue'yu açıklamalı veya ona bağlantı vermelidir.
* Pull request mümkün olduğunca tek bir amacı kapsamalıdır.
* Değişiklikler açık ve anlaşılır biçimde özetlenmelidir.
* Yeni özellik veya hata düzeltmelerinde uygun testler eklenmelidir.
* Pull request açılmadan önce ilgili testler ve kalite kontrolleri çalıştırılmalıdır.
* Pull request onaylandıktan sonra `main` branch'ine birleştirilmelidir.

## Test Kuralları

* Yeni backend özellikleri için uygun birim veya entegrasyon testleri yazılmalıdır.
* Yeni frontend davranışları için uygun testler eklenmelidir.
* Kritik kullanıcı akışları uçtan uca testlerle doğrulanmalıdır.
* Testler ilerleyen sprintlerde CI sürecinde otomatik olarak çalıştırılacaktır.

## Gizli Bilgiler ve Büyük Dosyalar

* API anahtarları, parolalar ve gerçek ortam değişkenleri repoya eklenmemelidir.
* Gizli bilgiler yalnızca yerel `.env` dosyasında tutulmalıdır.
* `.env.example` dosyası yalnızca örnek değerler içermelidir.
* Büyük veri setleri, eğitilmiş model ağırlıkları ve çalışma çıktıları GitHub'a yüklenmemelidir.
