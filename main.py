import Escape as e
import Room as r
import Constants as c

from rooms import E1_R1
from rooms import E1_R2
from rooms import E2_R1
from rooms import E2_R2
from rooms import E2_R3
from rooms import E3_R1
from rooms import E3_R2
from rooms import E3_R3
from rooms import E4_R1
from rooms import E4_R2
from rooms import E4_R3
from rooms import E5_R1
from rooms import E6_R1
from rooms import E7_R1
from rooms import E7_R2
from rooms import E8_R1
from rooms import E8_R2
from rooms import E9_R1
from rooms import E9_R2
from rooms import E10_R1
from rooms import E11_R1
from rooms import E11_R2
from rooms import E11_R3
from rooms import E11_R4
from rooms import E11_R5
from rooms import E12_R1
from rooms import E12_R2
from rooms import E12_R3
from rooms import E13_R1
from rooms import E13_R2
from rooms import E13_R3
from rooms import E13_R4
from rooms import E14_R1
from rooms import E15_R1
from rooms import E15_R2
from rooms import E15_R3
from rooms import E15_R4
from rooms import E15_R5
from rooms import E16_R1
from rooms import E16_R2
from rooms import E16_R3
from rooms import E17_R1
from rooms import E17_R2
from rooms import E17_R3
from rooms import E18_R1
from rooms import E18_R2
from rooms import E18_R3
from rooms import E19_R1
from rooms import E19_R2
from rooms import E19_R3
from rooms import E19_R4
from rooms import E20_R1
from rooms import E20_R2
from rooms import E21_R1
from rooms import E22_R1
from rooms import E23_R1
from rooms import E23_R2
from rooms import E23_R3
from rooms import E24_R1
from rooms import E24_R2
from rooms import E25_R1
from rooms import E25_R2
from rooms import E26_R1
from rooms import E27_R1
from rooms import E27_R2
from rooms import E27_R3
from rooms import E28_R1
from rooms import E28_R2
from rooms import E28_R3
from rooms import E28_R4
from rooms import E29_R1
from rooms import E29_R2
from rooms import E29_R3
from rooms import E29_R4
from rooms import E29_R5
from rooms import E29_R6
from rooms import E30_R1
from rooms import E30_R2
from rooms import E30_R3
from rooms import E30_R4
from rooms import E30_R5
from rooms import E30_R6
from rooms import E30_R7
from rooms import E30_R8
from rooms import E30_R9
from rooms import E30_R10
from rooms import E30_R11
from rooms import E31_R1
from rooms import E32_R1
from rooms import E32_R2
from rooms import E32_R3
from rooms import E33_R1
from rooms import E34_R1
from rooms import E35_R1
from rooms import E35_R2
from rooms import E35_R3
from rooms import E36_R1
from rooms import E36_R2
from rooms import E36_R3
from rooms import E37_R1
from rooms import E37_R2
from rooms import E38_R1
from rooms import E38_R2
from rooms import E39_R1
from rooms import E39_R2
from rooms import E40_R1
from rooms import E40_R2
from rooms import E41_R1
from rooms import E42_R1
from rooms import E43_R1
from rooms import E44_R1
from rooms import E44_R2
from rooms import E44_R3
from rooms import E45_R1

escapes = {
    'E1': e.Escape('Escape Room Roma 1', 'Roma', 'Via Benadir 2, 00199 Roma', '3924359562 - 3333727927 - 3465820365',
                   'https://www.escaperoomroma.it/', 41.9281492, 12.5203319,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG, c.ADVENTURE_TAG]), 'E1'),
    'E2': e.Escape('Escape Room Roma 2', 'Roma', 'Via del Casale Fainelli 69, 00157  Roma', '3924359562 - 3333727927 - 3465820365',
                   'https://www.escaperoomroma.it/', 41.9170743, 12.5462812,
                   c.SEPARATOR.join([c.MISTERY_TAG, c.ACTORS_TAG, c.ADVENTURE_TAG]), 'E2'),
    'E3': e.Escape('Magic Escape 1', 'Magic', 'Via Bolzano 40, 00198 Roma', '3701141293 - 3489266475',
                   'https://magicescape.it/', 41.9214719, 12.5136879,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E3'),
    'E4': e.Escape('Time Alive', 'Time Alive', 'Via Monte Nero 45, 00012 Guidonia', '3515413111 - 3346066844',
                   'https://www.time-alive.it/roma-2/', 41.9766136, 12.6153138,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E4'),
    'E5': e.Escape('Cogito Ergo Room', 'Cogito', 'Via Tiburtina 862, 00159 Roma', '0639727190 - 3668743988',
                   'https://cogitoergoroom.it/', 41.9181771, 12.5622175,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E5'),
    'E6': e.Escape('The Fear Escape Room', 'The Fear', 'Via Luigi Mancinelli 35, 00199 Roma', '3517039298',
                   'https://www.thefearescaperoom.it/', 41.9378439, 12.5120582,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E6'),
    'E7': e.Escape('Tribe Escape Room', 'Tribe', 'Via Derna 12, 00199 Roma', '0688651504 - 3407982795',
                   'https://www.tribescaperoom.it/', 41.9303491, 12.5171726,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E7'),
    'E8': e.Escape('Real Game', 'Real Game', 'Via Ugo Falena 9-11, 00137 Roma', '3917206160',
                   'http://www.escaperoomrealgame.it/', 41.9480525, 12.5545342,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E8'),
    'E9': e.Escape('Nox Escape', 'Nox', 'Via Pieve Ligure 25-27, 00168 Roma', '3276524107',
                   'https://www.nox-escape.com/', 41.9350597, 12.4199963,
                   c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E9'),
    'E10': e.Escape('La Porta Magica', 'Porta Magica', 'Viale Etiopia 18, 00199 Roma', '',
                    'http://www.laportamagicaescape.it/', 41.9325886, 12.5201052,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E10'),
    'E11': e.Escape('Fugacemente Alberone', 'Fugacemente', 'Via Gino Capponi 88, 00179 Roma', '3518321046',
                    'https://www.fugacemente.it/roma-alberone/', 41.8747715, 12.5174673,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E11'),
    'E12': e.Escape('Quest House', 'Quest House', 'Viale Regina Margherita 239/A, 00198 Roma', '0687650586 - 3891056519',
                    'https://questhouse.it/', 41.9126938, 12.5050896,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E12'),
    'E13': e.Escape('Adventure Rooms', 'Adventure', 'Via Molajoni 72, 00159 Roma', '3926938064',
                    'https://www.adventurerooms.it/roma/', 41.9071573, 12.537661,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E13'),
    'E14': e.Escape('Escape Room Roma 3', 'Roma', 'Via Fanfulla da Lodi 3, 00176 Roma', '3924359562 - 3333727927 - 3465820365',
                    'https://www.escaperoomroma.it/', 41.890973, 12.5279454,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E14'),
    'E15': e.Escape('Fugacemente Cinecittà', 'Fugacemente', 'Viale Palmiro Togliatti 70, 00173 Roma', '3711126805',
                    'https://www.fugacemente.it/cinecitta/', 41.8565997, 12.5693447,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E15'),
    'E16': e.Escape('Time Adventures', 'Time Adventures', 'Via dei Platani 100A, 00172 Roma', '3493780425',
                    'https://www.fugacemente.it/timeadventures/', 41.8809365, 12.5655152,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E16'),
    'E17': e.Escape('Fugacemente Anagnina', 'Fugacemente', 'Via del Fosso dell’Acqua Mariana 135, 00118 Roma', '3496233622',
                    'https://www.fugacemente.it/roma-anagnina/', 41.8182658, 12.6027993,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E17'),
    'E18': e.Escape('Fugacemente Colle Prenestino', 'Fugacemente', 'Via Calabritto 12, 00132 Roma', '3515833117',
                    'https://www.fugacemente.it/roma-colle-prenestino/', 41.89211, 12.6258395,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E18'),
    'E19': e.Escape('Fugacemente Tor Vergata', 'Fugacemente', 'Via Gioacchino Volpe 18, 00133 Roma', '3498254702',
                    'https://www.fugacemente.it/roma-tor-vergata/', 41.8385218, 12.6219024,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E19'),
    'E20': e.Escape('Fugacemente San Lorenzo', 'Fugacemente', 'Viale dello Scalo San Lorenzo 51, 00185 Roma', '3496233622',
                    'https://www.fugacemente.it/roma-san-lorenzo/', 41.8948605, 12.5149321,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E20'),
    'E21': e.Escape('Fugacemente Trastevere', 'Fugacemente', 'Via Francesco Benaglia 11, 00153 Roma', '3294630052',
                    'https://www.fugacemente.it/roma-trastevere/', 41.878528, 12.4642928,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E21'),
    'E22': e.Escape('Nox Escape 2', 'Nox', 'Viale Arcangelo Ghisleri 26, 00176 Roma', '3276524107',
                    'https://www.nox-escape.com/', 41.8862093, 12.5276016,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E22'),
    'E23': e.Escape('La Casa Degli Enigmi', 'Casa Degli Enigmi', 'Via Romanello da Forlì 18, 00176 Roma', '3791041282',
                    'http://www.lacasadeglienigmi.com/', 41.8911868, 12.5298234,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E23'),
    'E24': e.Escape('Exitus', 'Exitus', 'Via Quintilio Varo 75, 00174 Roma', '3457668894',
                    'https://escaperoomromaexitus.com/', 41.8547007, 12.5613896,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E24'),
    'E25': e.Escape('Secret Rooms', 'Secret', 'Via Mantellini 44, 00179 Roma', '0669366774',
                    'https://roma.secret-rooms.it/', 41.8733195, 12.5123541,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E25'),
    'E26': e.Escape('Get Out', 'Get Out', 'Via Bernardo Cennini 44, 00133 Roma', '3271054978',
                    'https://getoutroma.it/', 41.8259935, 12.5007254,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E26'),
    'E27': e.Escape('Magic Escape 2', 'Magic', 'Via Veio 35/C, 00183 Roma', '3701141293 – 3489266475',
                    'https://magicescape.it/', 41.8841663, 12.5077248,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E27'),
    'E28': e.Escape('Cronos', 'Cronos', 'Via Gregorio VII 205, 00165 Roma', '3884060735',
                    'https://roma.cronos.house/', 41.8953067, 12.4436591,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E28'),
    'E29': e.Escape('Game Over 1', 'Game Over', 'Via Giuseppe Marcora 3, 00153 Roma', '065894157 - 065810341 - 3386537546 - 3490726862',
                    'https://roma.escapegameover.it/index.php#', 41.8814827, 12.4669769,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E29'),
    'E30': e.Escape('Game Over 2', 'Game Over', 'Via Angelo Bargoni 44, 00153 Roma', '065894157 - 065810341 - 3386537546 - 3490726862',
                    'https://roma.escapegameover.it/index.php#', 41.8801284, 12.4665648,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E30'),
    'E31': e.Escape('Yellow Square', 'Yellow Square', 'Via Palestro 51, 00185 Rome', '064463554',
                    'https://www.the-yellow.com/escape-room/', 41.904704, 12.5022554,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E31'),
    'E32': e.Escape('The Door', 'The Door', 'Via Carlo Botta 11, 00184 Roma', '3899914580',
                    'http://www.thedoor.it/roma/index.php#il-gioco', 41.8913286, 12.4988266,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E32'),
    'E33': e.Escape('Zombie Escape', 'Zombie', 'Via Tortona 7, 00183 Roma', '0000000000',
                    'http://www.zombieescape.it/index.htm', 41.8796637, 12.5130724,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E33'),
    'E34': e.Escape('Locked', 'Locked', 'Via degli Scipioni 236, 00192 Roma', '3405236953 - 0695944279',
                    '', 41.9095395, 12.4621645,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E34'),
    'E35': e.Escape('Escape Campo dei Fiori', 'Campo dei Fiori', 'Vicolo delle Grotte 3, 00186 Roma', '3347261615',
                    'http://www.escapecampodeifiori.com/', 41.8948172, 12.4704218,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E35'),
    'E36': e.Escape('Experience Escape Room', 'Experience', 'Via dei Legatori 68/70, 00128 Roma', '3515115574',
                    'https://www.experienceescaperoom.it/', 41.7621569, 12.4635911,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E36'),
    'E37': e.Escape('Fugacemente Castel Gandolfo', 'Fugacemente', 'Via Michelangelo 1A, 00040 Castel Gandolfo', '3488442664 - 3463144420 - 3279054605',
                    'https://www.fugacemente.it/castelgandolfo/', 41.7275955, 12.614457,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E37'),
    'E38': e.Escape('Mentalmente', 'Mentalmente', 'Via Giuseppe Lunati 16, 00044 Frascati', '3473048770',
                    'http://www.mentalmenteescaperoom.it/', 41.8068178, 12.6785357,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E38'),
    'E39': e.Escape('Fugacity', 'Fugacity', 'Via Maremmana 15, 00030 San Cesareo', '3334568360 - 3397592091',
                    'http://www.fugacity.it/', 41.8200539, 12.775461,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E39'),
    'E40': e.Escape('Lucifer', 'Lucifer', 'Via Appia Pignatelli 235, 00178 Roma', '',
                    'http://www.luciferescaperoom.it/', 41.8431565, 12.5392839,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E40'),
    'E41': e.Escape('Joker Escape Room', 'Joker', 'Via Antonio Coppi 4C, 00179 Roma', '3342117822',
                    '', 41.8702714, 12.5136102,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E41'),
    'E42': e.Escape('La Casa Del Male', 'Casa Del Male', 'Via Appia Nuova 1305, 00178 Roma', '3518609064',
                    'https://www.lacasadelmale.it/', 41.8114527, 12.5719115,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E42'),
    'E43': e.Escape('Escape Room Ostia Roma', 'Ostia', 'Via Mar Rosso 335, 00122 Ostia', '3398018862',
                    '', 41.7314163, 12.3024346,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E43'),
    'E44': e.Escape('Escape Oddity', 'Oddity', 'Via Cristoforo Colombo 454A, 00145 Roma', '',
                    'https://www.escapeoddity.com/', 41.8507784, 12.4824413,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E44'),
    'E45': e.Escape('Horror Escape Room', 'Horror', 'Via Cornelio Magni 18, 00147 Roma', '3927249778',
                    '', 41.8656777, 12.4965895,
                    c.SEPARATOR.join([c.HORROR_TAG, c.ACTORS_TAG]), 'E45')
}

rooms = {
    'E1': {'R1': E1_R1.E1_R1(),
           'R2': E1_R2.E1_R2()},
    'E2': {'R1': E2_R1.E2_R1(),
           'R2': E2_R2.E2_R2(),
           'R3': E2_R3.E2_R3()},
    'E3': {'R1': E3_R1.E3_R1(),
           'R2': E3_R2.E3_R2(),
           'R3': E3_R3.E3_R3()},
    'E4': {'R1': E4_R1.E4_R1(),
           'R2': E4_R2.E4_R2(),
           'R3': E4_R3.E4_R3()},
    'E5': {'R1': E5_R1.E5_R1()},
    'E6': {'R1': E6_R1.E6_R1()},
    'E7': {'R1': E7_R1.E7_R1(),
           'R2': E7_R2.E7_R2()},
    'E8': {'R1': E8_R1.E8_R1(),
           'R2': E8_R2.E8_R2()},
    'E9': {'R1': E9_R1.E9_R1(),
           'R2': E9_R2.E9_R2()},
    'E10': {'R1': E10_R1.E10_R1()},
    'E11': {'R1': E11_R1.E11_R1(),
            'R2': E11_R2.E11_R2(),
            'R3': E11_R3.E11_R3(),
            'R4': E11_R4.E11_R4(),
            'R5': E11_R5.E11_R5()},
    'E12': {'R1': E12_R1.E12_R1(),
            'R2': E12_R2.E12_R2(),
            'R3': E12_R3.E12_R3()},
    'E13': {'R1': E13_R1.E13_R1(),
            'R2': E13_R2.E13_R2(),
            'R3': E13_R3.E13_R3(),
            'R4': E13_R4.E13_R4()},
    'E14': {'R1': E14_R1.E14_R1()},
    'E15': {'R1': E15_R1.E15_R1(),
            'R2': E15_R2.E15_R2(),
            'R3': E15_R3.E15_R3(),
            'R4': E15_R4.E15_R4(),
            'R5': E15_R5.E15_R5()},
    'E16': {'R1': E16_R1.E16_R1(),
            'R2': E16_R2.E16_R2(),
            'R3': E16_R3.E16_R3()},
    'E17': {'R1': E17_R1.E17_R1(),
            'R2': E17_R2.E17_R2(),
            'R3': E17_R3.E17_R3()},
    'E18': {'R1': E18_R1.E18_R1(),
            'R2': E18_R2.E18_R2(),
            'R3': E18_R3.E18_R3()},
    'E19': {'R1': E19_R1.E19_R1(),
            'R2': E19_R2.E19_R2(),
            'R3': E19_R3.E19_R3(),
            'R4': E19_R4.E19_R4()},
    'E20': {'R1': E20_R1.E20_R1(),
            'R2': E20_R2.E20_R2()},
    'E21': {'R1': E21_R1.E21_R1()},
    'E22': {'R1': E22_R1.E22_R1()},
    'E23': {'R1': E23_R1.E23_R1(),
            'R2': E23_R2.E23_R2(),
            'R3': E23_R3.E23_R3()},
    'E24': {'R1': E24_R1.E24_R1(),
            'R2': E24_R2.E24_R2()},
    'E25': {'R1': E25_R1.E25_R1(),
            'R2': E25_R2.E25_R2()},
    'E26': {'R1': E26_R1.E26_R1()},
    'E27': {'R1': E27_R1.E27_R1(),
            'R2': E27_R2.E27_R2(),
            'R3': E27_R3.E27_R3()},
    'E28': {'R1': E28_R1.E28_R1(),
            'R2': E28_R2.E28_R2(),
            'R3': E28_R3.E28_R3(),
            'R4': E28_R4.E28_R4()},
    'E29': {'R1': E29_R1.E29_R1(),
            'R2': E29_R2.E29_R2(),
            'R3': E29_R3.E29_R3(),
            'R4': E29_R4.E29_R4(),
            'R5': E29_R5.E29_R5(),
            'R6': E29_R6.E29_R6()},
    'E30': {'R1': E30_R1.E30_R1(),
            'R2': E30_R2.E30_R2(),
            'R3': E30_R3.E30_R3(),
            'R4': E30_R4.E30_R4(),
            'R5': E30_R5.E30_R5(),
            'R6': E30_R6.E30_R6(),
            'R7': E30_R7.E30_R7(),
            'R8': E30_R8.E30_R8(),
            'R9': E30_R9.E30_R9(),
            'R10': E30_R10.E30_R10(),
            'R11': E30_R11.E30_R11()},
    'E31': {'R1': E31_R1.E31_R1()},
    'E32': {'R1': E32_R1.E32_R1(),
            'R2': E32_R2.E32_R2(),
            'R3': E32_R3.E32_R3()},
    'E33': {'R1': E33_R1.E33_R1()},
    'E34': {'R1': E34_R1.E34_R1()},
    'E35': {'R1': E35_R1.E35_R1(),
            'R2': E35_R2.E35_R2(),
            'R3': E35_R3.E35_R3()},
    'E36': {'R1': E36_R1.E36_R1(),
            'R2': E36_R2.E36_R2(),
            'R3': E36_R3.E36_R3()},
    'E37': {'R1': E37_R1.E37_R1(),
            'R2': E37_R2.E37_R2()},
    'E38': {'R1': E38_R1.E38_R1(),
            'R2': E38_R2.E38_R2()},
    'E39': {'R1': E39_R1.E39_R1(),
            'R2': E39_R2.E39_R2()},
    'E40': {'R1': E40_R1.E40_R1(),
            'R2': E40_R2.E40_R2()},
    'E41': {'R1': E41_R1.E41_R1()},
    'E42': {'R1': E42_R1.E42_R1()},
    'E43': {'R1': E43_R1.E43_R1()},
    'E44': {'R1': E44_R1.E44_R1(),
            'R2': E44_R2.E44_R2(),
            'R3': E44_R3.E44_R3()},
    'E45': {'R1': E45_R1.E45_R1()}
}

escapes_objs = []
for k1 in escapes.keys():
    v1 = escapes[k1]
    e_r = []
    for k2 in rooms[k1].keys():
        e_r.append(rooms[k1][k2].get_room_object())
    v1.set_rooms(e_r)
    escapes_objs.append(v1.get_escape_object())

if __name__ == '__main__':
    print({c.ESCAPES_TAG: escapes_objs})
