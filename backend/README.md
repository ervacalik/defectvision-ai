# Backend

DefectVision AI projesinin backend uygulaması bu klasörde bulunur. Backend, FastAPI kullanılarak geliştirilecektir ve ilerleyen aşamalarda görüntü analizi, kusur tespiti, kullanıcı işlemleri ve veri yönetimi için API uç noktalarını sağlayacaktır.

## Teknolojiler

- Python 3.11+
- FastAPI
- Uvicorn

## Gereksinimler

Bilgisayarınızda Python 3.11 veya daha yeni bir sürümün kurulu olması gerekir.

## Kurulum

Önce backend klasörüne geçin:

```bash
cd backend
```

Sanal ortam oluşturun:

```bash
python -m venv venv
```

Git Bash kullanıyorsanız sanal ortamı aktifleştirin:

```bash
source venv/Scripts/activate
```

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

## Uygulamayı Çalıştırma

Geliştirme sunucusunu başlatmak için:

```bash
uvicorn app.main:app --reload
```

Uygulama varsayılan olarak şu adreste çalışır:

```text
http://127.0.0.1:8000
```

## Kullanılabilir Endpoint’ler

| Adres | Açıklama |
| --- | --- |
| `/health` | Backend servisinin çalıştığını doğrular. |
| `/docs` | FastAPI tarafından otomatik oluşturulan Swagger API dokümantasyonunu açar. |

## Notlar

- Sanal ortam klasörü (`venv`) GitHub’a gönderilmez.
- Yeni bir terminal açıldığında paket kurulumu veya uygulamayı çalıştırmadan önce sanal ortam tekrar aktifleştirilmelidir.
- Veritabanı, kimlik doğrulama ve iş mantığı sonraki görevlerde eklenecektir.