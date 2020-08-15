import pandas as pd
from sklearn.metrics.pairwise import cosine_distances

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split


def train_tfidf(filepath, col_name, stopwords=None):
    df = pd.read_csv(filepath, encoding='iso-8859-1')
    tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words=stopwords)
    tfidf_matrix = tfidf.fit_transform(df[col_name].values.astype('U'))
    return tfidf, tfidf_matrix


def train_bow(filepath, col_name):
    df = pd.read_csv(filepath, encoding='iso-8859-1')
    bow = CountVectorizer().fit(df[col_name])
    return bow


def document_prediction(query, filepath, col_name, tfidf, tfidf_matrix):
    df = pd.read_csv(filepath, encoding='iso-8859-1')
    vec = tfidf.transform([query])
    dist = cosine_distances(vec, tfidf_matrix)
    result_series = dist.argsort()[0, :10]
    result_list = result_series.tolist()
    result = df[col_name][result_list]
    document_list = result.tolist()
    return document_list


STOPWORDS = [
    'ada', 'adalah', 'adanya', 'adapun',
    'agak',
    'agaknya',
    'agar',
    'akan',
    'akankah',
    'akhir',
    'akhiri',
    'akhirnya',
    'aku',
    'akulah',
    'amat',
    'amatlah',
    'anda',
    'andalah',
    'antar',
    'antara',
    'antaranya',
    'apa',
    'apaan',
    'apabila',
    'apakah',
    'apalagi',
    'apatah',
    'artinya',
    'asal',
    'asalkan',
    'atas',
    'atau',
    'ataukah',
    'ataupun',
    'awal',
    'awalnya',
    'bagai',
    'bagaikan',
    'bagaimana',
    'bagaimanakah',
    'bagaimanapun',
    'bagi',
    'bagian',
    'bahkan',
    'bahwa',
    'bahwasanya',
    'baik',
    'bakal',
    'bakalan',
    'balik',
    'banyak',
    'bapak',
    'baru',
    'bawah',
    'beberapa',
    'begini',
    'beginian',
    'beginikah',
    'beginilah',
    'begitu',
    'begitukah',
    'begitulah',
    'begitupun',
    'bekerja',
    'belakang',
    'belakangan',
    'belum',
    'belumlah',
    'benar',
    'benarkah',
    'benarlah',
    'berada',
    'berakhir',
    'berakhirlah',
    'berakhirnya',
    'berapa',
    'berapakah',
    'berapalah',
    'berapapun',
    'berarti',
    'berawal',
    'berbagai',
    'berdatangan',
    'beri',
    'berikan',
    'berikut',
    'berikutnya',
    'berjumlah',
    'berkali-kali',
    'berkata',
    'berkehendak',
    'berkeinginan',
    'berkenaan',
    'berlainan',
    'berlalu',
    'berlangsung',
    'berlebihan',
    'bermacam',
    'bermacam-macam',
    'bermaksud',
    'bermula',
    'bersama',
    'bersama-sama',
    'bersiap',
    'bersiap-siap',
    'bertanya',
    'bertanya-tanya',
    'berturut',
    'berturut-turut',
    'bertutur',
    'berujar',
    'berupa',
    'besar',
    'betul',
    'betulkah',
    'biasa',
    'biasanya',
    'bila',
    'bilakah',
    'bisa',
    'bisakah',
    'boleh',
    'bolehkah',
    'bolehlah',
    'buat',
    'bukan',
    'bukankah',
    'bukanlah',
    'bukannya',
    'bulan',
    'bung',
    'cara',
    'caranya',
    'cukup',
    'cukupkah',
    'cukuplah',
    'cuma',
    'dahulu',
    'dalam',
    'dan',
    'dapat',
    'dari',
    'daripada',
    'datang',
    'dekat',
    'demi',
    'demikian',
    'demikianlah',
    'dengan',
    'depan',
    'di',
    'dia',
    'diakhiri',
    'diakhirinya',
    'dialah',
    'diantara',
    'diantaranya',
    'diberi',
    'diberikan',
    'diberikannya',
    'dibuat',
    'dibuatnya',
    'didapat',
    'didatangkan',
    'digunakan',
    'diibaratkan',
    'diibaratkannya',
    'diingat',
    'diingatkan',
    'diinginkan',
    'dijawab',
    'dijelaskan',
    'dijelaskannya',
    'dikarenakan',
    'dikatakan',
    'dikatakannya',
    'dikerjakan',
    'diketahui',
    'diketahuinya',
    'dikira',
    'dilakukan',
    'dilalui',
    'dilihat',
    'dimaksud',
    'dimaksudkan',
    'dimaksudkannya',
    'dimaksudnya',
    'diminta',
    'dimintai',
    'dimisalkan',
    'dimulai',
    'dimulailah',
    'dimulainya',
    'dimungkinkan',
    'dini',
    'dipastikan',
    'diperbuat',
    'diperbuatnya',
    'dipergunakan',
    'diperkirakan',
    'diperlihatkan',
    'diperlukan',
    'diperlukannya',
    'dipersoalkan',
    'dipertanyakan',
    'dipunyai',
    'diri',
    'dirinya',
    'disampaikan',
    'disebut',
    'disebutkan',
    'disebutkannya',
    'disini',
    'disinilah',
    'ditambahkan',
    'ditandaskan',
    'ditanya',
    'ditanyai',
    'ditanyakan',
    'ditegaskan',
    'ditujukan',
    'ditunjuk',
    'ditunjuki',
    'ditunjukkan',
    'ditunjukkannya',
    'ditunjuknya',
    'dituturkan',
    'dituturkannya',
    'diucapkan',
    'diucapkannya',
    'diungkapkan',
    'dong',
    'dua',
    'dulu',
    'empat',
    'enggak',
    'enggaknya',
    'entah',
    'entahlah',
    'guna',
    'gunakan',
    'hal',
    'hampir',
    'hanya',
    'hanyalah',
    'hari',
    'harus',
    'haruslah',
    'harusnya',
    'hendak',
    'hendaklah',
    'hendaknya',
    'hingga',
    'ia',
    'ialah',
    'ibarat',
    'ibaratkan',
    'ibaratnya',
    'ibu',
    'ikut',
    'ingat',
    'ingat-ingat',
    'ingin',
    'inginkah',
    'inginkan',
    'ini',
    'inikah',
    'inilah',
    'itu',
    'itukah',
    'itulah',
    'jadi',
    'jadilah',
    'jadinya',
    'jangan',
    'jangankan',
    'janganlah',
    'jauh',
    'jawab',
    'jawaban',
    'jawabnya',
    'jelas',
    'jelaskan',
    'jelaslah',
    'jelasnya',
    'jika',
    'jikalau',
    'juga',
    'jumlah',
    'jumlahnya',
    'justru',
    'kala',
    'kalau',
    'kalaulah',
    'kalaupun',
    'kalian',
    'kami',
    'kamilah',
    'kamu',
    'kamulah',
    'kan',
    'kapan',
    'kapankah',
    'kapanpun',
    'karena',
    'karenanya',
    'kasus',
    'kata',
    'katakan',
    'katakanlah',
    'katanya',
    'ke',
    'keadaan',
    'kebetulan',
    'kecil',
    'kedua',
    'keduanya',
    'keinginan',
    'kelamaan',
    'kelihatan',
    'kelihatannya',
    'kelima',
    'keluar',
    'kembali',
    'kemudian',
    'kemungkinan',
    'kemungkinannya',
    'kenapa',
    'kepada',
    'kepadanya',
    'kesampaian',
    'keseluruhan',
    'keseluruhannya',
    'keterlaluan',
    'ketika',
    'khususnya',
    'kini',
    'kinilah',
    'kira',
    'kira-kira',
    'kiranya',
    'kita',
    'kitalah',
    'kok',
    'kurang',
    'lagi',
    'lagian',
    'lah',
    'lain',
    'lainnya',
    'lalu',
    'lama',
    'lamanya',
    'lanjut',
    'lanjutnya',
    'lebih',
    'lewat',
    'lima',
    'luar',
    'macam',
    'maka',
    'makanya',
    'makin',
    'malah',
    'malahan',
    'mampu',
    'mampukah',
    'mana',
    'manakala',
    'manalagi',
    'masa',
    'masalah',
    'masalahnya',
    'masih',
    'masihkah',
    'masing',
    'masing-masing',
    'mau',
    'maupun',
    'melainkan',
    'melakukan',
    'melalui',
    'melihat',
    'melihatnya',
    'memang',
    'memastikan',
    'memberi',
    'memberikan',
    'membuat',
    'memerlukan',
    'memihak',
    'meminta',
    'memintakan',
    'memisalkan',
    'memperbuat',
    'mempergunakan',
    'memperkirakan',
    'memperlihatkan',
    'mempersiapkan',
    'mempersoalkan',
    'mempertanyakan',
    'mempunyai',
    'memulai',
    'memungkinkan',
    'menaiki',
    'menambahkan',
    'menandaskan',
    'menanti',
    'menanti-nanti',
    'menantikan',
    'menanya',
    'menanyai',
    'menanyakan',
    'mendapat',
    'mendapatkan',
    'mendatang',
    'mendatangi',
    'mendatangkan',
    'menegaskan',
    'mengakhiri',
    'mengapa',
    'mengatakan',
    'mengatakannya',
    'mengenai',
    'mengerjakan',
    'mengetahui',
    'menggunakan',
    'menghendaki',
    'mengibaratkan',
    'mengibaratkannya',
    'mengingat',
    'mengingatkan',
    'menginginkan',
    'mengira',
    'mengucapkan',
    'mengucapkannya',
    'mengungkapkan',
    'menjadi',
    'menjawab',
    'menjelaskan',
    'menuju',
    'menunjuk',
    'menunjuki',
    'menunjukkan',
    'menunjuknya',
    'menurut',
    'menuturkan',
    'menyampaikan',
    'menyangkut',
    'menyatakan',
    'menyebutkan',
    'menyeluruh',
    'menyiapkan',
    'merasa',
    'mereka',
    'merekalah',
    'merupakan',
    'meski',
    'meskipun',
    'meyakini',
    'meyakinkan',
    'minta',
    'mirip',
    'misal',
    'misalkan',
    'misalnya',
    'mula',
    'mulai',
    'mulailah',
    'mulanya',
    'mungkin',
    'mungkinkah',
    'nah',
    'naik',
    'namun',
    'nanti',
    'nantinya',
    'nyaris',
    'nyatanya',
    'oleh',
    'olehnya',
    'pada',
    'padahal',
    'padanya',
    'pak',
    'paling',
    'panjang',
    'pantas',
    'para',
    'pasti',
    'pastilah',
    'penting',
    'pentingnya',
    'per',
    'percuma',
    'perlu',
    'perlukah',
    'perlunya',
    'pernah',
    'persoalan',
    'pertama',
    'pertama-tama',
    'pertanyaan',
    'pertanyakan',
    'pihak',
    'pihaknya',
    'pukul',
    'pula',
    'pun',
    'punya',
    'rasa',
    'rasanya',
    'rata',
    'rupanya',
    'saat',
    'saatnya',
    'saja',
    'sajalah',
    'saling',
    'sama',
    'sama-sama',
    'sambil',
    'sampai',
    'sampai-sampai',
    'sampaikan',
    'sana',
    'sangat',
    'sangatlah',
    'satu',
    'saya',
    'sayalah',
    'se',
    'sebab',
    'sebabnya',
    'sebagai',
    'sebagaimana',
    'sebagainya',
    'sebagian',
    'sebaik',
    'sebaik-baiknya',
    'sebaiknya',
    'sebaliknya',
    'sebanyak',
    'sebegini',
    'sebegitu',
    'sebelum',
    'sebelumnya',
    'sebenarnya',
    'seberapa',
    'sebesar',
    'sebetulnya',
    'sebisanya',
    'sebuah',
    'sebut',
    'sebutlah',
    'sebutnya',
    'secara',
    'secukupnya',
    'sedang',
    'sedangkan',
    'sedemikian',
    'sedikit',
    'sedikitnya',
    'seenaknya',
    'segala',
    'segalanya',
    'segera',
    'seharusnya',
    'sehingga',
    'seingat',
    'sejak',
    'sejauh',
    'sejenak',
    'sejumlah',
    'sekadar',
    'sekadarnya',
    'sekali',
    'sekali-kali',
    'sekalian',
    'sekaligus',
    'sekalipun',
    'sekarang',
    'sekarang',
    'sekecil',
    'seketika',
    'sekiranya',
    'sekitar',
    'sekitarnya',
    'sekurang-kurangnya',
    'sekurangnya',
    'sela',
    'selain',
    'selaku',
    'selalu',
    'selama',
    'selama-lamanya',
    'selamanya',
    'selanjutnya',
    'seluruh',
    'seluruhnya',
    'semacam',
    'semakin',
    'semampu',
    'semampunya',
    'semasa',
    'semasih',
    'semata',
    'semata-mata',
    'semaunya',
    'sementara',
    'semisal',
    'semisalnya',
    'sempat',
    'semua',
    'semuanya',
    'semula',
    'sendiri',
    'sendirian',
    'sendirinya',
    'seolah',
    'seolah-olah',
    'seorang',
    'sepanjang',
    'sepantasnya',
    'sepantasnyalah',
    'seperlunya',
    'seperti',
    'sepertinya',
    'sepihak',
    'sering',
    'seringnya',
    'serta',
    'serupa',
    'sesaat',
    'sesama',
    'sesampai',
    'sesegera',
    'sesekali',
    'seseorang',
    'sesuatu',
    'sesuatunya',
    'sesudah',
    'sesudahnya',
    'setelah',
    'setempat',
    'setengah',
    'seterusnya',
    'setiap',
    'setiba',
    'setibanya',
    'setidak-tidaknya',
    'setidaknya',
    'setinggi',
    'seusai',
    'sewaktu',
    'siap',
    'siapa',
    'siapakah',
    'siapapun',
    'sini',
    'sinilah',
    'soal',
    'soalnya',
    'suatu',
    'sudah',
    'sudahkah',
    'sudahlah',
    'supaya',
    'tadi',
    'tadinya',
    'tahu',
    'tahun',
    'tak',
    'tambah',
    'tambahnya',
    'tampak',
    'tampaknya',
    'tandas',
    'tandasnya',
    'tanpa',
    'tanya',
    'tanyakan',
    'tanyanya',
    'tapi',
    'tegas',
    'tegasnya',
    'telah',
    'tempat',
    'tengah',
    'tentang',
    'tentu',
    'tentulah',
    'tentunya',
    'tepat',
    'terakhir',
    'terasa',
    'terbanyak',
    'terdahulu',
    'terdapat',
    'terdiri',
    'terhadap',
    'terhadapnya',
    'teringat',
    'teringat-ingat',
    'terjadi',
    'terjadilah',
    'terjadinya',
    'terkira',
    'terlalu',
    'terlebih',
    'terlihat',
    'termasuk',
    'ternyata',
    'tersampaikan',
    'tersebut',
    'tersebutlah',
    'tertentu',
    'tertuju',
    'terus',
    'terutama',
    'tetap',
    'tetapi',
    'tiap',
    'tiba',
    'tiba-tiba',
    'tidak',
    'tidakkah',
    'tidaklah',
    'tiga',
    'tinggi',
    'toh',
    'tunjuk',
    'turut',
    'tutur',
    'tuturnya',
    'ucap',
    'ucapnya',
    'ujar',
    'ujarnya',
    'umum',
    'umumnya',
    'ungkap',
    'ungkapnya',
    'untuk',
    'usah',
    'usai',
    'waduh',
    'wah',
    'wahai',
    'waktu',
    'waktunya',
    'walau',
    'walaupun',
    'wong',
    'yaitu',
    'yakin',
    'yakni',
    'yang',
    'i',
    'me',
    'my',
    'myself',
    'we',
    'our',
    'ours',
    'ourselves',
    'you',
    "you're",
    "you've",
    "you'll",
    "you'd",
    'your',
    'yours',
    'yourself',
    'yourselves',
    'he',
    'him',
    'his',
    'himself',
    'she',
    "she's",
    'her',
    'hers',
    'herself',
    'it',
    "it's",
    'its',
    'itself',
    'they',
    'them',
    'their',
    'theirs',
    'themselves',
    'what',
    'which',
    'who',
    'whom',
    'this',
    'that',
    "that'll",
    'these',
    'those',
    'am',
    'is',
    'are',
    'was',
    'were',
    'be',
    'been',
    'being',
    'have',
    'has',
    'had',
    'having',
    'do',
    'does',
    'did',
    'doing',
    'a',
    'an',
    'the',
    'and',
    'but',
    'if',
    'or',
    'because',
    'as',
    'until',
    'while',
    'of',
    'at',
    'by',
    'for',
    'with',
    'about',
    'against',
    'between',
    'into',
    'through',
    'during',
    'before',
    'after',
    'above',
    'below',
    'to',
    'from',
    'up',
    'down',
    'in',
    'out',
    'on',
    'off',
    'over',
    'under',
    'again',
    'further',
    'then',
    'once',
    'here',
    'there',
    'when',
    'where',
    'why',
    'how',
    'all',
    'any',
    'both',
    'each',
    'few',
    'more',
    'most',
    'other',
    'some',
    'such',
    'no',
    'nor',
    'not',
    'only',
    'own',
    'same',
    'so',
    'than',
    'too',
    'very',
    's',
    't',
    'can',
    'will',
    'just',
    'don',
    "don't",
    'should',
    "should've",
    'now',
    'd',
    'll',
    'm',
    'o',
    're',
    've',
    'y',
    'ain',
    'aren',
    "aren't",
    'couldn',
    "couldn't",
    'didn',
    "didn't",
    'doesn',
    "doesn't",
    'hadn',
    "hadn't",
    'hasn',
    "hasn't",
    'haven',
    "haven't",
    'isn',
    "isn't",
    'ma',
    'mightn',
    "mightn't",
    'mustn',
    "mustn't",
    'needn',
    "needn't",
    'shan',
    "shan't",
    'shouldn',
    "shouldn't",
    'wasn',
    "wasn't",
    'weren',
    "weren't",
    'won',
    "won't",
    'wouldn',
    "wouldn't",
    '!',
    '"',
    '#',
    '$',
    '%',
    '&',
    "'",
    '(',
    ')',
    '*',
    '+',
    ',',
    '-',
    '.',
    '/',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    '@',
    '[',
    '\\',
    ']',
    '^',
    '_',
    '`',
    '{',
    '|',
    '}',
    '~']
