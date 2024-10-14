Bu proje ekip içerisinde gerçekleştirilecek diğer projelerdeki kullanıcı adı ve şifre gibi kişisel verilerin 
proje içerisinde şifrelenerek kullanılmasını sağlamak ve şifrelenmiş veriyi sadece kullanıcın kendisinin
sahip olduğu key ile çözebileceği şekilde tasarlanmıştır. Projedeki amaç yazılan kodlar içerisinde genellikle
yer alan veri tabanı kullanıcı bilgileri gibi hassa ve kişisel bilgilerin güvenliğini sağlamaktır.


Proje kullanım adımları:
1- İlk defaya mahsus olarak random key generator modülü ile kişisel bir key üretilmelidir.
(key'in güvenliği ile alakalı bir sorun söz konusu olmadığı sürece değiştirmeniz gerekmez.)
2- Bu oluşturulan key kullanılarak encryption_decryption modülü içerisindeki encryptor fonksiyonu
kullanılarak kullanıcı adı ve şifre encrypt edilir.
3- Bilgilerin kullanılacağı projede encrypt edilmiş kullanıcı adı ve şifreyi key verisi ile decrypte etmek
için encryption_decryption modülü içerisindeki decryptor fonksiyonu kullanılır.