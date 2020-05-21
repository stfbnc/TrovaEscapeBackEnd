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

escapes = {
    'E1': e.Escape('Escape Room Roma 1', 'Via Benadir 2, 00199 Roma', '3924359562 - 3333727927 - 3465820365',
              'https://www.escaperoomroma.it/', 41.9281492, 12.5203319, 'E1'),
    'E2': e.Escape('Escape Room Roma 2', 'Via del Casale Fainelli 69, 00157  Roma', '3924359562 - 3333727927 - 3465820365',
              'https://www.escaperoomroma.it/', 41.9170743, 12.5462812, 'E2'),
    'E3': e.Escape('Magic Escape 1', 'Via Bolzano 40, 00198 Roma', '3701141293 - 3489266475',
              'https://magicescape.it/', 41.9214719, 12.5136879, 'E3'),
    'E4': e.Escape('Time Alive', 'Via Monte Nero 45, 00012 Guidonia', '3515413111 - 3346066844',
              'https://www.time-alive.it/roma-2/', 41.9766136, 12.6153138, 'E4'),
    'E5': e.Escape('Cogito Ergo Room', 'Via Tiburtina 862, 00159 Roma', '0639727190 - 3668743988',
              'https://cogitoergoroom.it/', 41.9181771, 12.5622175, 'E5'),
    'E6': e.Escape('The Fear Escape Room', 'Via Luigi Mancinelli 35, 00199 Roma', '3517039298',
              'https://www.thefearescaperoom.it/', 41.9378439, 12.5120582, 'E6'),
    'E7': e.Escape('Tribe Escape Room', 'Via Derna 12, 00199 Roma', '0688651504 - 3407982795',
              'https://www.tribescaperoom.it/', 41.9303491, 12.5171726, 'E7'),
    'E8': e.Escape('Real Game', 'Via Ugo Falena 9-11, 00137 Roma', '3917206160',
              'http://www.escaperoomrealgame.it/', 41.9480525, 12.5545342, 'E8'),
    'E9': e.Escape('Nox Escape', 'Via Pieve Ligure 25-27, 00168 Roma', '3276524107',
              'https://www.nox-escape.com/', 41.9350597, 12.4199963, 'E9'),
    'E10': e.Escape('La Porta Magica', 'Viale Etiopia 18, 00199 Roma', '',
               'http://www.laportamagicaescape.it/', 41.9325886, 12.5201052, 'E10'),
    'E11': e.Escape('Fugacemente Alberone', 'Via Gino Capponi 88, 00179 Roma', '3518321046',
               'https://www.fugacemente.it/roma-alberone/', 41.8747715, 12.5174673, 'E11'),
    'E12': e.Escape('Quest House', 'viale Regina Margherita 239/A, 00198 Roma', '0687650586 - 3891056519',
               'https://questhouse.it/', 41.9126938, 12.5050896, 'E12'),
    'E13': e.Escape('Adventure Rooms', 'Via Molajoni 72, 00159 Roma', '3926938064',
               'https://www.adventurerooms.it/roma/', 41.9071573, 12.537661, 'E13'),
    'E14': e.Escape('Escape Room Roma 3', 'Via Fanfulla da Lodi 3, 00176 Roma', '3924359562 - 3333727927 - 3465820365',
               'https://www.escaperoomroma.it/', 41.890973, 12.5279454, 'E14'),
    'E15': e.Escape('Fugacemente Cinecittà', 'Viale Palmiro Togliatti 70, 00173 Roma', '3711126805',
               'https://www.fugacemente.it/cinecitta/', 41.8565997, 12.5693447, 'E15'),
    'E16': e.Escape('Time Adventures', 'Via dei Platani 100A, 00172 Roma', '3493780425',
               'https://www.fugacemente.it/timeadventures/', 41.8809365, 12.5655152, 'E16'),
    'E17': e.Escape('Fugacemente Anagnina', 'Via del Fosso dell’Acqua Mariana 135, 00118 Roma', '3496233622',
               'https://www.fugacemente.it/roma-anagnina/', 41.8182658, 12.6027993, 'E17'),
    'E18': e.Escape('Fugacemente Colle Prenestino', 'Via Calabritto 12, 00132 Roma', '3515833117',
               'https://www.fugacemente.it/roma-colle-prenestino/', 41.89211, 12.6258395, 'E18'),
    'E19': e.Escape('Fugacemente Tor Vergata', 'Via Gioacchino Volpe 18, 00133 Roma', '3498254702',
               'https://www.fugacemente.it/roma-tor-vergata/', 41.8385218, 12.6219024, 'E19'),
    'E20': e.Escape('Fugacemente San Lorenzo', 'Viale dello Scalo San Lorenzo 51, 00185 Roma', '3496233622',
               'https://www.fugacemente.it/roma-san-lorenzo/', 41.8948605, 12.5149321, 'E20'),
    'E21': e.Escape('Fugacemente Trastevere', 'Via Francesco Benaglia 11, 00153 Roma', '3294630052',
               'https://www.fugacemente.it/roma-trastevere/', 41.878528, 12.4642928, 'E21'),
    'E22': e.Escape('Nox Escape 2', 'Viale Arcangelo Ghisleri 26, 00176 Roma', '3276524107',
               'https://www.nox-escape.com/', 41.8862093, 12.5276016, 'E22'),
    'E23': e.Escape('La Casa Degli Enigmi', 'Via Romanello da Forlì 18, 00176 Roma', '3791041282',
               'http://www.lacasadeglienigmi.com/', 41.8911868, 12.5298234, 'E23'),
    'E24': e.Escape('Exitus', 'Via Quintilio Varo 75, 00174 Roma', '3457668894',
               'https://escaperoomromaexitus.com/', 41.8547007, 12.5613896, 'E24'),
    'E25': e.Escape('Secret Rooms', 'Via Mantellini 44, 00179 Roma', '0669366774',
               'https://roma.secret-rooms.it/', 41.8733195, 12.5123541, 'E25'),
    'E26': e.Escape('Get Out', 'Via Bernardo Cennini 44, 00133 Roma', '3271054978',
               'https://getoutroma.it/', 41.8259935, 12.5007254, 'E26'),
    'E27': e.Escape('Magic Escape 2', 'Via Veio 35/C, 00183 Roma', '3701141293 – 3489266475',
               'https://magicescape.it/', 41.8841663, 12.5077248, 'E27'),
    'E28': e.Escape('Cronos', 'Via Gregorio VII 205, 00165 Roma', '3884060735',
               'https://roma.cronos.house/', 41.8953067, 12.4436591, 'E28'),
    'E29': e.Escape('Game Over 1', 'Via Giuseppe Marcora 3, 00153 Roma', '065894157 - 065810341 - 3386537546 - 3490726862',
               'https://roma.escapegameover.it/index.php#', 41.8814827, 12.4669769, 'E29'),
    'E30': e.Escape('Game Over 2', 'Via Angelo Bargoni 44, 00153 Roma', '065894157 - 065810341 - 3386537546 - 3490726862',
               'https://roma.escapegameover.it/index.php#', 41.8801284, 12.4665648, 'E30'),
    'E31': e.Escape('Yellow Square', 'Via Palestro 51, 00185 Rome', '064463554',
               'https://www.the-yellow.com/escape-room/', 41.904704, 12.5022554, 'E31'),
    'E32': e.Escape('The Door', 'Via Carlo Botta 11, 00184 Roma', '3899914580',
               'http://www.thedoor.it/roma/index.php#il-gioco', 41.8913286, 12.4988266, 'E32'),
    'E33': e.Escape('Zombie Escape', 'Via Tortona 7, 00183 Roma', '0000000000',
               'http://www.zombieescape.it/index.htm', 41.8796637, 12.5130724, 'E33'),
    'E34': e.Escape('Locked', 'Via degli Scipioni 236, 00192 Roma', '3405236953 - 0695944279',
               '', 41.9095395, 12.4621645, 'E34'),
    'E35': e.Escape('Escape Campo dei Fiori', 'Vicolo delle Grotte 3, 00186 Roma', '3347261615',
               'http://www.escapecampodeifiori.com/', 41.8948172, 12.4704218, 'E35'),
    'E36': e.Escape('Experience Escape Room', 'Via dei Legatori 68/70, 00128 Roma', '3515115574',
               'https://www.experienceescaperoom.it/', 41.7621569, 12.4635911, 'E36'),
    'E37': e.Escape('Fugacemente Castel Gandolfo', 'Via Michelangelo 1A, 00040 Castel Gandolfo', '3488442664 - 3463144420 - 3279054605',
               'https://www.fugacemente.it/castelgandolfo/', 41.7275955, 12.614457, 'E37'),
    'E38': e.Escape('Mentalmente', 'Via Giuseppe Lunati 16, 00044 Frascati', '3473048770',
               'http://www.mentalmenteescaperoom.it/', 41.8068178, 12.6785357, 'E38'),
    'E39': e.Escape('Fugacity', 'Via Maremmana 15, 00030 San Cesareo', '3334568360 - 3397592091',
               'http://www.fugacity.it/', 41.8200539, 12.775461, 'E39'),
    'E40': e.Escape('Lucifer', 'Via Appia Pignatelli 235, 00178 Roma', '',
               'http://www.luciferescaperoom.it/', 41.8431565, 12.5392839, 'E40'),
    'E41': e.Escape('Joker Escape Room', 'Via Antonio Coppi 4C, 00179 Roma', '3342117822',
               '', 41.8702714, 12.5136102, 'E41'),
    'E42': e.Escape('La Casa Del Male', 'Via Appia Nuova 1305, 00178 Roma', '3518609064',
               'https://www.lacasadelmale.it/', 41.8114527, 12.5719115, 'E42'),
    'E43': e.Escape('Escape Room Ostia Roma', 'Via Mar Rosso 335, 00122 Ostia', '3398018862',
               '', 41.7314163, 12.3024346, 'E43'),
    'E44': e.Escape('Escape Oddity', 'Via Cristoforo Colombo 454A, 00145 Roma', '',
               'https://www.escapeoddity.com/', 41.8507784, 12.4824413, 'E44'),
    'E45': e.Escape('Horror Escape Room', 'Via Cornelio Magni 18, 00147 Roma', '3927249778',
               '', 41.8656777, 12.4965895, 'E45')
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
    'E5': {},
    'E6': {},
    'E7': {},
    'E8': {},
    'E9': {},
    'E10': {},
    'E11': {},
    'E12': {},
    'E13': {},
    'E14': {},
    'E15': {},
    'E16': {},
    'E17': {},
    'E18': {},
    'E19': {},
    'E20': {},
    'E21': {},
    'E22': {},
    'E23': {},
    'E24': {},
    'E25': {},
    'E26': {},
    'E27': {},
    'E28': {},
    'E29': {},
    'E30': {},
    'E31': {},
    'E32': {},
    'E33': {},
    'E34': {},
    'E35': {},
    'E36': {},
    'E37': {},
    'E38': {},
    'E39': {},
    'E40': {},
    'E41': {},
    'E42': {},
    'E43': {},
    'E44': {},
    'E45': {}
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
