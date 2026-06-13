"""Links collection.

This file is part of spasylki-az.

spasylki-az is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License v3 (LGPLv3) as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

spasylki-az is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License v3 (LGPLv3) for
more details. In file LICENSE which should came with a package, or look at it
in the repo, see <https://github.com/measles/spasylki-az/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3
(LGPLv3) along with Łatynkatar. If not, see <https://www.gnu.org/licenses/>.

:copyright: (c) 2026 Andrej Zacharevicz: https://github.com/measles/spasylki-az
"""

from dataclasses import dataclass


@dataclass
class Section:
    """Dataclass representing a whole section of the collection.

    :param name: Name of the section
    :type name: str
    :param description: Description of the section
    :type description: str
    :param links: Links in the section tuple(link, description)
    :type links: tuple[tuple[str, str], ...]
    """

    name: str
    description: str
    links: tuple[tuple[str, str], ...]


pravapis = (
    (
        "https://languagetool.org/ ",
        "Цэлы камбайн па праверцы правапісу розных моў, у тым ліку беларускай. Ёсць плагіны для браўзэраў. "
        "Часта ім карыстаюся.",
    ),
    (
        "https://bnkorpus.info/spell.html",
        'Праверка правапісу ад праекту "Беларускі N-корпус"',
    ),
    (
        "https://bnkorpus.info/grammar.be.html",
        "Граматычная база Корпусу. Не вычэрпны даведнік, але бывае вельмі карысным для пошука форм слова.",
    ),
    (
        "https://bnkorpus.info/korpus.be.html",
        "Пошук слова па корпусе беларускіх тэкстаў.",
    ),
    (
        "https://slounik.org",
        "Процьма розных слоўнікаў і энцыклапедый. Але варта ўлічваць, што ў 20-30 мінулага стагоддзя было шмат "
        "эксперыментаў з мовай, так што слоўнікі таго перыяду трэба ўспрымаць з лёгкім скепсісам.",
    ),
    ("https://verbum.by", "Карысны набор слоўнікаў."),
    (
        "https://antykalka.org",
        "Цікавы слоўнік, які дае адпаведнікі рускаму слову, тлумачачы значэнне кожнага беларускага адпаведніка",
    ),
)

knihi = (
    ("https://knihauka.com", 'Анлайн-кнігарня "Кнігаўка" выдавецтва Андрэя Янушкевіча'),
    ("https://allegro.pl/uzytkownik/Knihauka", '"Кнігаўка" на Allegro.pl'),
    (
        "https://www.koskabooks.com/",
        "Выдавецтва дзіцячых кніг. Нажаль, пакуль кнігі даступныя толькі ў электронным выглядзе.",
    ),
    (
        "https://gutenbergpublisher.eu/",
        "Еўрапейскае беларускае выдавецтва Gutenberg Publisher ",
    ),
    ("https://skarynapress.com/", "Выдавецтва Скарына"),
    (
        "https://knihi.by/",
        "Добрая анлайн-кнігарня з гісторыяй і традыцыямі. Працуе ў Мінску, але высылае і за мяжу. Калі браць досыць "
        "шмат кніг, то кошт высылкі не такі балючы.",
    ),
    (
        "https://kamunikat.shop/?v=9b7d173b068d",
        "Кнігарня выдавецтва пры фондзе Камунікат. Вельмі раю!",
    ),
)

biblijateki = (
    (
        "https://kamunikat.org/",
        "Вялізны праект па збору ўсіх матэрыялаў (кнігі, аўдыёкнігі, газэты, часопісы, відэа і іншае) выданых "
        "па-беларуску ці пра Беларусь на іншых мовах. Ад 2021 яшчэ і выдае папяровы кнігі.",
    ),
    (
        "https://knihi.com/",
        "Наколькі я ведаю, старэйшая беларускай анлайн-бібліятэка (працуе ад 1996 года). Процьма самых розных "
        "выданняў.",
    ),
    (
        "https://audiobooks.by/",
        "Каталог беларускіх аўдыё-кніг. Вельмі раю, калі любіце гэты фармат.",
    ),
    (
        "https://knizhnyvoz.com/app/",
        "Аўдыёвыдавецтва, якое рупліва і старана агучвае беларускія кнігі. Кнігі можна паслухаць на сайце, альбо праз "
        "іх мабільныя аплікацыі.",
    ),
    (
        "https://knihi-online.com/",
        "Вельмі цікавая анлайн-бібліятэка, дзе ў PDF даступныя шмат якія выбітныя класічныя кнігі і шмат што з "
        "цікавага сучаснага.",
    ),
)

kanviertary = (
    (
        "https://baltoslav.eu/lat/index.php?mova=bx",
        "Лацінізатар ад праекта БалтаСлав. Апроч, уаласна, канвертэра змяшчае яшчэ цікавыя матэрыяла пра лацінку.",
    ),
    (
        "https://slounik.org/lat",
        "Нажаль, не цалкам цункцыянальны канвертэр ад Слоўніка. ",
    ),
)

dzieciam = (
    (
        "https://www.youtube.com/@gavarun-cartoons",
        "Гаварун — мультфільмы па-беларуску. Выдатны канал з перакладамі мульікаў і мультсерыялаў на беларускую мову. "
        "Якасныя і цікавыя мульцікі, асабіста вельмі люблю 'Хамфа'. 'Паляўнічых на цмовакаў', 'Пакаё' і 'Эрнэст і "
        "Селестына' ",
    ),
    (
        "https://gavarun.by/p/support",
        "Падтрымаць рэгулярны выпуск перакладаў і арыгінальных праектаў Гаваруна для дзяцей. Падтрымайце, калі вы "
        "глядзіце Гаваруна, падтрымайце калі вы не глядзіце, але хочаце дапамагчы беларускім дзеям. Ці нават калі ўсё "
        "абрыдла — падтрымайце, зрабіце добрую справу.",
    ),
    (
        "https://www.koskabooks.com/",
        "Выдавецтва дзіцячых кніг. Нажаль, пакуль кнігі даступныя толькі ў электронным выглядзе.",
    ),
    (
        "https://www.youtube.com/@baybusby",
        'Канал з вельмі цікавымі дзіцячымі відэа: тут і відэаадаптацыя коміксаў "Асцярожна дзеці" і "Казкі з '
        'Маляванычам"',
    ),
    (
        "https://www.youtube.com/@vozhykibel3467",
        "Блізняты-важаняты. Выдатны і вельмі мілы мультсерыял на беларускай. Нажаль, выпуск перарваны, але я "
        "спадзяюся некалі ўбачыць працяг.",
    ),
    (
        "https://www.youtube.com/@bielamult",
        "Беламульт. Яшчэ адзін даволі вялікі рэсурс з мульцікамі па-беларуску.",
    ),
    (
        "https://knizhnyvoz.com/app/",
        "Аўдыёвыдавецтва, якое рупліва і старана агучвае беларускія кнігі. Шмат кніг для дзяцей і падлеткаў. Ёсць "
        "мабільныя аплікацыі, але можна слухаць і з браўзэра.",
    ),
    (
        "https://youtube.com/playlist?list=PLZvkfSDlL6yjg2IVRkUVXxh1P740mK2D1",
        'Пяцьдзесят серый "Свінкі Пэпы" па-беларуску.',
    ),
    (
        "https://dzietkam.knihi.com/",
        "Краіна казак. Процьма казак, дыяфільмаў, мульцікаў, песенек, калыханак. Нажаль, у мяне не працуе з сайту, "
        "але можна паставіць на тэлефон аплікацыю, там ўсё будзе.",
    ),
    (
        "https://youtube.com/playlist?list=PLZvkfSDlL6yjg2IVRkUVXxh1P740mK2D1",
        "English з Наталкай. Цудоўныя заняткі па ангельскай для вучняў пятых класаў ад Наталлі Харытанюк.",
    ),
    (
        "https://www.youtube.com/@historyjabielarusi",
        "Гісторыя Беларусі | Альгерд ужо ня той. Гістарычны канал для дзяцей, бацькоў і настаўнікаў.",
    ),
)

filmy = (
    (
        "https://youtube.com/@gavarun-movie",
        "Цяпер можна глядзець фільмы і серыялы ў цудоўным перакладзе Гаваруна. Не забывайце падтрымаць праект грашыма!",
    ),
    (
        "https://kinakipa.site/",
        "Праект Кінакіпа і яго вялізная калекцыя фільмаў для ўсёй сям'і па-беларуску.",
    ),
    (
        "https://anibel.net/",
        "Вялікая калекцыя анімэ (перакладзеных голасам і тытрамі) і фільмаў па-беларуску.",
    ),
    ("https://baravik.org/", "Беларускі торэнт-трэкер."),
)

kniznyja_kluby = (
    (
        "https://t.me/bookclub_tbm",
        "Анлайн кніжны клуб Таварыства Беларускай Мовы імя Францішка Скарыны",
    ),
    (
        "https://t.me/cytalniachat",
        "Чат кнігарні беларускай кнігі ў Вільні, маюць свой анлайн кніжны клуб.",
    ),
    ("https://t.me/klub_lichtaryk", '"Ліхтарык" - беларускі кніжны клуб у Варшаве'),
    (
        "https://t.me/wroclaw_knizhny_klub",
        'Кніжны клуб "Уроцлаў" — беларускі кніжны клуб ва Уроцлаве',
    ),
    (
        "https://t.me/KniznyklubPoznan",
        "Кніжны клуб створаны ў рамах Беларускага размоўнага клубу ў Познані",
    ),
    (
        "https://t.me/+H0yAIR9EAqk2ZWZi",
        "Беларускі кніжны клуб у Аўстраліі. Анлайн кніжны клуб з сустрэчамі анлайн увечары па Мельбурне.",
    ),
)
szkoly = (
    ("https://belshkola.org/", "Беларуская школа ў Варшаве."),
    ("http://aksiarodak.tilda.ws/", "Беларуская школа ў Батумі."),
    (
        "https://www.shkolaravenskaga.pl/",
        "Беларуская школа мастацтваў імя М. Равенскага ў Варшаве.",
    ),
    ("https://imschool.pl/school_main_by", 'Школа "Я дома" у Варшаве.'),
    ("https://skorinosgimnazija.lt/by", "Віленская гімназія імя Францыска Скарыны."),
    (
        "http://bialorushajnowka.pl/",
        "II Агульнаaдуkaцыйны Лiцэй З Дадатковым Навучаннем Беларускай Мовы Ў Гайнаўцы.",
    ),
    (
        "https://trojka.szkolnastrona.pl",
        "Базавая школа №3 з дадатковым вывучэннем беларускай мовы ім. Я. Кастыцжвіча у Бельску Падляскім",
    ),
    (
        "https://sp4.edu.bialystok.pl/pl/",
        "Базавая школа №4 ім. сібіракоў у Беластоку.",
    ),
)


SECTIONS = (
    Section(name="Filmy", description="Фільмы па-беларуску", links=filmy),
    Section(
        name="Biblijateki",
        description="Анлайн бібліятэкі беларускіх кніг",
        links=biblijateki,
    ),
    Section(
        name="Knihi",
        description="Выдавецтвы і кнігарні дзе можна купіць беларускія кнігі за мяжою",
        links=knihi,
    ),
    Section(name="Dzieciam", description="Для дзяцей па-беларуску", links=dzieciam),
    Section(
        name="Szkoły",
        description="Беларускія школы па-за межамі Беларусі",
        links=szkoly,
    ),
    Section(
        name="Slouniki",
        description="Праверка правапісу, даведнікі, слоўнікі",
        links=pravapis,
    ),
    Section(name="Kanviertary", description="Канвертары ў лацінку", links=kanviertary),
    Section(name="kniznyja_kluby", description="Кніжныя клубы", links=kniznyja_kluby),
)
