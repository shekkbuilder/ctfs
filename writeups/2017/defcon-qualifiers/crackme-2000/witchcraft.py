import socket
import sys
import base64

answers = {
'0009931a87a0353c1377ae073e62e2dbabf3e4249680ec751cfde1fe14d635d8': 'bright as jewel',
'01b22b4c67a408a08c07b7c3af5a807512cc6dc41380d889f14605dc3bbcda43': 'y Cast?. She vanishes, then reappears, forty ',
'022ac0f92120d6464fdf34a6884369dcc8049db7dde3021dea1d2b610d4f5560': 'ars sequence had already inspired a',
'02bd830274ed4a6550456eb092a5124701d1d1216bea20ee86e70f7a78ef1729': ' down to work for me, they\'re all real',
'034c1558890a94b675a5b7e7fcd882a855b369b0e292bc498eafd43600e03211': ' any technological measures t',
'03b2dcde6fbc4f9cb96ce1de4cbccd73960c196f6345e6dee66da0a9a89bf2d0': ' did the',
'04af9eb95699dc1889af849607364a8b42ef9680203e977a844736e673c5730d': 'ue. There was no way th',
'074fb3ade4c4e34a28a2c660ba50df8ef8270065d09af30b7c3d3335bc2a25bb': 'ort Wilderness C',
'0758278d2d5e48c205a909b2dd8aa5b8250ebe6f3ebbfcc68d81be7a4ce67ae4': 'r conditioning an',
'078d42b8ee9dfed4287117f7e2c42bbf705f11b5332496c4774bcd53fb6feba3': ' for me. My parents had brou',
'082e0e683e60af601d6a63837a9ec776b9d0dd26e1bd0c151123fe2176b73900': 'ot one trick: restore from backup. You\'',
'09c173b23c98450a904ec7152ef0f8b86eddb675c541e1a6148dae8b10065de5': 'iful when s',
'0a141435fef54ddd64eaaa9862873254c52a94812478095d3ca93ed82bce40d0': 'd swap out a dead bot for a backup in fi',
'0d88ee8a1943652170db2f47cf5d9049a954aaf71fbe8150489a467ddf8e7564': 'e here are _you?_" Debra smiled condesce',
'0f20260818b740cb3a3499c0e271665d04fd94f2d93b651891bf622c74427e7e': 'mer, everything star',
'13c617620bdeeedcafd1015d05089650b6bd0dad212945e32802f7012f8a7349': 'hile mutteri',
'14cbafd67b6bcadfe1a5f54a53c0bc82f511d1fa35fcdac8579f889fc70d7cc7': 'you want to, that\'s yo',
'1894322bce7ac10bac38a4dee3ac8b099482617e238c199c9364d0f9e8b86099': 't exchange any u',
'18b8148b8c67b8f79f583834941e1a1ecb1757d418dfb420d47c20dfe1946114': ' dust from shore',
'1939a0bdd93c18e9f2ee85156078a1f61eb3b2b372681747dd0bac2e932b0e37': '"That\'s not really my area," Tim said. "I\'m a',
'19e75078797ffb695ebd24c8961afdc096577324ec16cef402bd959f42cd0be5': 'er-geniuses would come up wit',
'1b8369fc08527b1b802bc32a16e3f556ef414ec20fccad37201cf46b6759c367': 'e, is it really so much to ask? Fine. Wait wh',
'1d1d35c540ec8e1dfa0fa10de9093fed68d7642df2e3af50c733782ce1749ba0': ', everything else gets ',
'1d4f1f913a87459fc7fb6315b1c857f795f8a62fbe4d8314601438abce2812f4': 'ese days. They\'re too coope',
'1de0db0d389302bfd74505a5758e4a79fd420a697280695a8d376fc4d0aaeb61': 'azine # Imagine you woke up one day and Walt',
'1e856e1aa01d6fb8cdfa8e57d65a40ff9bfa07b19d7bebd904fc108f6dfdf223': 'a parabolic hol',
'206d25645cce23be6c3fcea4e6fc7ffc1f17d3be8db5ce2cf4162a65b5bd7d52': 'LICENSE OR ',
'21751c364cd37cf575d6f2cfd729063b2f9e8c7a7338154211921c208032f7f5': '" he said, into his pal',
'22e712eaa04591f648e10ca81aad56b777fface88357e9d554ed8903840320f6': 'e." I pinged my Whuffie. I ',
'2413b4b996ea11ffba37502566fe4ecf9ae5b22c6168cd756db79f979d321b9f': 'ce Sterling Author, The Hacker Cra',
'24f676017c65141c75837c1f00a54631cff76c1ab0f98c3e9292404c51669878': ', sit by',
'27852969b34cd0753c3f804cb75f4f841659ebd05ed389754cf03cf70060d94a': 'nty that',
'2840c66bf6b96debd17bad9fa87470390218f81cd98562a7310f4fa17e408f70': 's something',
'2a72b3da55c2f3c65904da6d66bf762af777166179248ee2da502335675357bf': 'ive duty. ',
'2b84a2c833a40334d6c913d03075573f5638e1e8919efc4afaa9dee875ddbe39': 'y dead trees and ticking clocks',
'2c8a1aef07fb3a4c39cc6e2178a470c7486209ad9cd04dacfff6e2d8438d6a6a': 'goon just isn\'t good show. In the meantime',
'2cefcf0885853e9e047505ffd2a23184186c92e60e8708b293669316a2075c65': 'rface. # The doc looked sour a',
'2da11e2a61cb087efece8eb1007be620c6a486be0622895cecc98f75c3585e56': ' that we stand a good chance of m',
'3025bcd63191eb3ef3ecf23cee036ef08451c88e82b1b89d6d8315359199c1cd': 'es and the torch-lightin',
'3115af689eecb161ccad41639f7755879a349bc9be872d5ed8ce967b38e8da23': 'one or more',
'3201d37bed0a38b233966cb65307a5ce8ead5ac77b990eaa3d8ce06962e725f3': 'w this up? Without warning, she',
'334e8cb295bdfda29d36d775e8cd8f171b77e8d12f107ac299af7aa02c14ee6b': 'ch mind. ',
'3577d17f8156477f4f9fdda31d590d5e982a6290b8635a6012c5bce01b8a3356': 'o Debra. Do',
'369c0f69852bf1ad7ceaa9e1aae871744a93132fcf8b8de11ae0180b58b1c5a6': 's done qu',
'37ba530c5244c18611ae29984cf262aa9dae9b878d4259474fe9fbe5799f9c52': 'd buy you security and peace. By',
'3984a3e3aa49b3a0d4121ff7781b7cfa17caccf22960f5724646c99649f82a24': 'embered ',
'3aa9f7c85efd40ce0f5c9a69de02132cd0aae12de72af9f2b598397020720f32': 'hrone. "You liked it?" Tim said. I no',
'3ae25ed954fbabe6199e072727093cbb2b08f2c92dde6a7396bb2307484441e2': 'd a few commands an',
'3c930cc3e90e4a3c12094d2f61764238e2c57932442856abfecb5d37f4677f8c': 'I resolved not ',
'3d14b5b1d08047d26034e67043d2432e00bcbf9572b15ebd8cbb88d1589c54f9': 'd them with a spacehand\'s grace, vaulting ',
'3ded12af84559a24e397d94aaf31c2fcc44c7d6045f780bc8ac3e3555a7c118f': ' the ferry d',
'3e850cdea18a3a8e6bc20e63dccfaa4492d2627a74df7a5e83fb103b271c36c1': 's the righ',
'41fa6f61e4277e4c781caf615650e6c058bb8746587415b42511580d3558e406': '-- put up a token resistance. Before the da',
'43fb61084d95ce5953f7d08beb6b84f9b95047cdb3a112ed92e9613d1e1e8657': 't, and I k',
'4454e05ee70edc519895d1b66423d64efbab288df2706d685022b1162f0ac77a': 'orow@craphoun',
'44a49eed3e4a9cd4ed19b3a0e173b2aaac269cc7daddb16f53739311bc9d4f08': 'e-of-thumb?aid would have',
'45d3eddb484838ccb2fbb6734f6fc4d600c9c6b1ce1f6901615d1ec9c7a06d63': ' we can ',
'46624512f0db33a0be6b25a8771df434cf1ed91b01a91e5024d0d7104b516071': 'body, I probably wouldn\'t be flexibl',
'47dcf74284a1d4c8bb01b20184c32077c2cf933173aaad046fa53001db332f80': ' world that',
'4833726090edb7f6ced596a3479c5192f2190ec15c68c434158afd6ce082c445': 'hoc can speak." I took a',
'484e3cdd34d01bcdcb3472a21f43ce84cfa6eca6644841124292cb1067b695d9': 'l tricks back in t? old days. "All right, ',
'485ad14a4bc0c696c0595deafc0f948f17d73ef03dc1e30c0c9362447b6d9377': 'ing heavi',
'498b131f9c2ffda17e4cbd21159afebf587206b6d921a4ba899f257926bbde56': ' salt w?er was balm, ',
'4b4aa75c5bf9eaaf067bea816691d45c3cfa7726cb60612f97934940bc01dc12': 't find her',
'4cf83660f5692093926f857e716ae6b32999afe71b4f3e50a802159a4e10b3f3': 'g from his hips. He scuttled around ',
'4f5c1f4364502103afd331b48fac3aebe603a082540857ba4cf3fce901eea7c3': 'HOUT WARRANTIES OF ANY K',
'52aba6c00934d0ef61ab53dff2ad546f09d86c32b7f6f31aba8a93a01cbf099c': 'st into the living room',
'55ef13f853bd1bc2410649915dd6c918cfc8f9677660d5c59323e9229b3dc20a': 'ing to make this last as l',
'5700650a1aedb70f2da8682cdc739a30a67803d4b1162e63e6ac6b121210af74': 'l pocket. To the layperson, such a specim',
'58fac970adbee7b68e5c083c6a53ee2400e2658480216086b48872abf398ca8b': ' the steps two at a time',
'5972818f405cdfc2b614bb0f9461ca38e1d677f61ee1897672201e7472693d08': 'r the terms of this L',
'5b2de0c5ecd6b6b1ceca53186c94abc230b50b32818df795361cade2b6a22562': 'ring dust in the parlor. "Congratulations',
'5c449d1a4adaa16e9bf56a9f4d947b95928122a7f1f99814649daa606b352649': 'et me try out this experiment. All that said, ',
'5d6b91b060edf9a061d3cd7401225449007fbe169cd38d9539c55802794e3e15': 'ght as jewe',
'602ca487ea9b9266292249d768aa3e2d487acb72b189b70e40d3fad0e81af189': 'ace \'em ',
'6137fe5f95067c99100716d571db085b0469038860bd067681cfb4bf6d48366c': 'a week before ret',
'6165bd9066ee7c8d2ced5f01f92064abbca84cdb428cc550526fb93620586485': 'x full houses waiting here ',
'619f0915349cf97fbfe1a22eae8162a1716d6faeab69d38656c7ec6a4edc58fd': '\'s wait. The Hall _never_ drew crowds like t',
'62191423265f4a023c368591989880e7a4b4625f6b87b8a9df3892ad78bd3a97': ', isn\'t it?" I said, finally. "I suppose so," ',
'6532329823c9be447f2c25915d63b73559f37d3117bf288fb30ed61d279bbd70': ' muggy winter evening, ',
'6577fdb2474b1a499922c6544b0c1888eedb28e6d48d0003d958dfa24ac16c08': 'Tonight. Aft',
'66bbbe5711c05d98597b2cd3f78260cf882734fefd38d2bb99805e2bdf878f3b': 'Look, you don\'t have',
'679d5203883a4446f55ae9f705a8e90e6f95a8f49046c9d745d9c121ee7cc79d': ' out of it." I dropped my pap',
'696b7f32928baa930786fde198de6e46adac34855c6188c30194c62c34a9eedd': 't is, the process is _short_. In a couple mo',
'6a275e4cf26ed8c0782761889572ee9266700b186412a6827d77febaca233bef': ' pretenders to the throne',
'6bd896b2dc9a6961a73c5c6d5c171349083f6b2f9aa36c4a05196e281670af63': ' rolled in. I was offline',
'6c52c5129e714f9502bbb6b1533030a5b3106149f579ec7192e4b4a215e5abdb': 'd a short story collection: A Place So Fo',
'6f74f434b994bffe9ae065ad8afcdf098b4f8bbc5ae98239dc6986177d93b7e8': '\'m meeting so many interesting p',
'70c5e8e091b0ff24332039d582d5515f8f0c766082032febdfc32ff37fac7d68': 'hat',
'71f4c8c9ea64953e0fa8e79b5b582289a61b44cbd3a977ac1f2208e827aeeb58': 'ge his reaction. He had his pok',
'725bca32b15560ef9c5315b28b1bda3bbaafd1bb9201c0e1540f231bbb105ad0': 'ea. I worked alongside Dan, using h',
'7310213ea86544197eb20ee715dd4bdb0ad0fb050d0aa117dfdcb55e06a4944f': ' cou',
'7511f67dbf365d78c15b0bb96bc485007b1c7292d7c3b011abaa7f06fd7ba2fa': 'ne of the designers squirt some plans at y',
'75be293844774b77c2a884c4f75c94d9ee771a0b66a8712a7db89ee5925a7d52': 'ince my boyhood',
'79dc570fec78e5f40fab590ab0f067270873a470275e57a42d01409ef0f791ea': 'that Tim fi',
'7aefd6b0cfbf63d2e6c109e7ebfa4400c5613b97de0658c220a51671d09192ac': 'vulnerable ',
'7b5aede7aaa1a2a202e297ddf5bd0de5abe98817b5819d835b8c6e9048723b00': 'is place -- all the',
'7cbabc3778af11098b9d031aacfa218ab6420bb344c4896bbfa76977acc8c922': ' know Dan, r?ht?" Debra nodded at him. "Oh, s',
'7e9b07f0ae43f705c5d0fef529a3f8ff5d640ea9e5b677d6996e719c3d9d5aaa': 'agues the rest of us, like lower-back pain, i',
'81f5d9422370c3bad5eea50b6747d01c43c5b691b6f185c2d24ce9e4e37a7c4f': ' youth when I first met him,',
'83c1f9280594aa38ee033d2161c23f254aa654bae42e5253d7935f28a5c5337f': 'he face of a Park that changed almost',
'8633370b04026131d112d328b94a17e0613d28c6f6faa86034d9b3952d757a29': 'king angrily to Debra. Hickor?Jackson in th',
'88f14048fc92253774a5091a61b2b09ddb3dc9935895a57625129fc06a9adecb': 'e as I switched on public access. He dumpe',
'8a7c7af43f8a410fab7280e187b79a4bce0a1e41bb84292bdd21a3988ca25f36': 'backup into my new body, a ',
'8aa407a2667f452c6c15f820f899d329665eb0d692553a80e2d3c4dd1d073f6c': 'egendary on the station, that crazy pair th',
'8ba32ecb6bd3a8037dff5ea43ff1da29e9405fefc1687731138ce524074adef6': ' arcane gizmos, or formed ',
'8c31a9c65af34ef2c475cc9b5625ffe49fec153c776ce81826f4480d90b49d20': 'bit of a plunge. Today, in coi',
'8d72924c68238b4dcaeefd99ccaf2c2dd2243ed4f6b21ee855908abb2cd504cd': 'h the Park, ',
'8e0ad5ac7b3bb101c1772d7fb004ffd32aa3e0d2f5765e70d572b9127b606b06': 'y widening. He tried',
'8e45974cd86d5de8fa2170c8574f8ee11383d91ad1fc3f844ddc917583bb2ee3': ' the legendary missi',
'8fbf0924ce1644a9eeff120f94379981cfb328d018d64361dc77ee904f2f4b16': 'atching the',
'90fb1d356e4eab1afe5fd878683e4f0263cdb5e3b79a9644bc64794e18039554': 'e, and I felt suddenly light and cool and re',
'9204d1bdf92bf9af51a5b008768f886e40a37aabde3485e2b8de7dfc0264136f': 'nged. Again and again, I came back to the Park',
'92315b9dc25a2cc5bcb7458359f833233f3ee5997807d021d9a9c00b9c10ee43': 'No clocks in the infirmary, and no internal',
'93e1520b9d1e9810e10bc0d63f89a25903a98aeabde684617f666cc2b481d758': 'a cigarette from',
'960bc9b92fa42a1ad340df4470328fda693a63449f2e3f5e5b918031365c16d3': 'osed to be the authority on med',
'9616cd7227c5c07490ff7d85b1ae8e96dcc555a10faff82e184ba9bae3e57bcb': 'ork that cons',
'973b151527ae8d7d7f9925d8c28737bb3ff5ef5418343ab2bee557968e172f3f': ' discussion. "Okay,',
'975e58ecfb4eeb260a001591c8b5911c2a5104844bfea68a57494511256df4f2': ' Hall of Presidents, and wha',
'98f86a42d1ea606155c9c7c11307a5a413724142510e02ed5ab9ac46759ef76c': 'rte?to grasp how important the M',
'9a1a340245f5b5982ccebfff5a331849271c0bce50f91c9acca5fbb556fc6200': 'd to bring my',
'9aec57008b6b55424aa028346f5054c3e9bedbbd30414255728c7696409458ec': 'ne to any of the absolutely inan',
'9b8ea9a515bbddc14dea02b1a911cc0fd0046d41132267bec6e94f0f9f67147b': 'dered if it ',
'9bf267e6fa8e49c22c2b7a79ed340b6ba92f364207efe8c3ef73455422bc64d3': 'minute ride, hammering one after anothe',
'9c0895592787ab667fc104bc59aff4047f08f653ab10c78c0310587aeaaeaa78': 't as the girl with the pith helmet draws a s',
'9cf187425bcaffc5d58cb7252e489d83c57c611c4df5c93a936825ebee7c4156': 'e out, a positive',
'9d327fdee6b98e944269dd39a321c04bd12065fd8fc67fc62b854b6a1f279bdf': 'l, forgotten on the back seat of m',
'9f42f93cd137031b563ca50e92499d491aa676f64784aace5c7e8ca14675a6da': 'e in no ',
'9f54fadffb8f806d341618f31bf6d6967ce7a1056391445aaaf38e89b0a802d9': 'r agenda. Ad-hoc? Hell, c',
'9f83388eb2b6f36537a8ce89996cbe5af7fb5d16bc457b445422c80efedf5373': 'use the water fountains and stand in line. If I',
'a0781099934057270543df82301e148b19ac7f659b1778ef8479db4f43b9627a': 'rawl forward to the next service hatch, near t',
'a103b2652ab8407bb552f7f8a0d0e43ac4cb1865498959ccc27fec3449081735': 'icycles and sped towards Suneep',
'a18505793a6463b8dd99fcc627fc9c4ed3caa7bef4b2f84671b2d0f0df56135f': 'd doing an incredible j',
'a30079e05a786fbf93a59764ad793cae8e9852b6f624dad1060e8f41b4655fc1': 'ad-hocs i',
'a39f7f3bb3212cacd69e4153ae1665a64dd2a653ccec906487b7ab16c76cdf5b': 'l it up to max dispersi',
'a4af376d58feaf92c24f94aaeb49ee3a7efc52127acd852a850653f8dbd0aad6': 't a decade before, when they\'d had ',
'a58e9032bd1abb1c0af57573cb4384327408a3c2a04a256185ee3a857efb35a2': ' I nearly',
'a8dbed41dd0d772e61897413e8235ce1c925f9717af8fa45fa2a2f469ca32cf3': ' Work or upon the Work',
'a9d06bb5e0f97328f0089be1c3d345705070326cf5dfff01f3f96e35ffc19172': 'the tube, then felt his hand groping u',
'ab0137cee60c9d51fa0c8c9be188c23882c53366b891d29c762f497a10873e8c': 'use was perfect: the ghosts that whirled ',
'ad45b02cb1d1a5176c5d2ae0046f07643582c710c8fb29b1ac14fee716c6ed77': 'r feather-shedding du',
'ae72df16448a2567ec90f04c7fa65de0452fc84e152c7b71998c34b8e7a7fe26': 'nd bifocals, h',
'b143f9fb45a0a94f275c85d48a1d4838e2be2896414ed5fa6abc09bb2613be5e': 'fore I co',
'b416de5fb23362133bc809e1cffcf91414f66c1ac4386dcd514728d77e0ed1a8': ' human re',
'b4a20620b28acf6f57df6ab5f27c98763ed885ef40c12839fcaf53d5c0743b93': 'o! There ar?\'t any junkies anymore!" He s',
'b867f26d5f2843cf24b4ce73ace61ef4fb359c83520d02be550affea442955d3': 'wed us out the door and to our next encoun',
'b899c78078ad59b4a35fd52a3fe3c0bbdc88e4db3b62570f8440068086892da5': 'uldn\'t bring myself to turn away. "Shhh," ',
'b8f8971ed7a45ec0418a13ae3c32a2256933c31e804198f0e60156f2dd8b3ca0': 'k though, not until we ',
'ba8a507b858262b142d88f6367808bf760693e840eda95128d5741d798ac6200': ' bush-league j',
'bb198e7c8d993c7d4a5125ff0b6c4c7f3f74917ae8d347576fb323577e3320ad': 'sing th?entire text of',
'bc54fc4392313cd9008186f52cf7254f11aad33912fffc8276d3041038d5667c': '\'When we were growing up,',
'bc6e0d9143de80c9407ab406e677f76c85593aac9b99f0f6b49de00bf752d7fa': 'e, I swear. _A ?use divided ',
'bd50148d768825767f40f9fa013b593020d9692d597926a695a464e0d2395ec6': 'd thence to a heavy, exposed Fa',
'bedb18d1e552e99a93341ff51b2250704495ac416addc275f534642a66b0f76b': 'ckstage, ',
'bf24c0545088c5edff5d8a5510436275b19f41f7e3147cdf526d47b2b6eda04b': '\'d get him',
'bffe51e46a6ea7d447cac302111a4f0bac1884a014250aaa2be61cc4318a9196': 'vered in a fine, r',
'c0fde8083556067d8924495bd2128d31091f5e43d935ff4ff3d7efdde1d49daf': 'ie -- piles of it, an',
'c14ca6a5067eb2202ad7b438c3586efbb73347b37b089bed140864acababecb5': 'over the Hall of Presidents.',
'c2530bf31e56d6f1ef4e36eec622ff93c05e8bc419b24d15763a5c7d0dfc76b5': 'eople I\'d m? when I was doing my m',
'c25763007a73536181b1c23e1e3ce2365d8828d163fd2add5dfd52c3a03194aa': 'nsees must gi',
'c38b8b50b7dea67605b412ec3d542e14f9d25a0ead85dfb7b30d69ec4f1ef5d5': 'ked up her father\'s bo',
'c7a49c19344efe3c4f3cb648c5d7a44ef33c19f4b903a525eac691c329708783': 'uld carry a lot of we',
'c83d7af9f084f4aeebf4f4fe9f0a1fe341687d1929dbacc771330fdd1dc00ad1': 'uld\'ve run a deep',
'c926a585cc5d3253506dd892552ad2999dbcbcbc34141bd1aef8575ed27b4bb3': 'oared back a collective, "Hi, Lil!" and lau',
'c939e0ad537ab86b5b8f59871fca78a444fa3a1036425f5dcd6d4c0a23910c5c': 'st of us were still a lit',
'ca260f859012aa9262f71c47ceb50447d91e72caf6321e402984052d2fecece9': 'one the arithmetic and ensured themsel',
'ceb6c4384f0307be0ba257586ae8e3396772e2c5395171f0b4e4c08ece75d734': 'ped, there to count the monkey-card',
'cfca47487d750a89e882504c8c6d745f0c953b420dd7d786427c864ac80385ec': 'le and we ca',
'cffbe68fd1c2858a3a16ad441dcfe5186efea542b4d76a080286065949a620eb': 'creativecommons.org/licenses',
'd0bf56d3c8d02a85474082bec30f08f7ec02895db8e5fc6486fecadbd0b8516a': 'c class, ',
'd9388e16b2376755120581a059a53bd43c4770bbc9963584dce35110bd1187b8': 'er, a ro',
'd9d44e0ed577db24072e2abef6468f14db31a0ea88d7afe6cb668f229c337a65': 'are in no way affected by the?b',
'da8527534aa80c2282f428ef43bdbcdd8c89acee5e80d2fdecedf123b0b6d67a': 'sion have come to seem',
'da92359b736fdc3d0d1c7688e9ebd02b67406d4260823514cd849eaed0ec9c13': ' of your voluntary nervous proc',
'dba05b9b7e15384e5ff231dfce69c64e9589f48f7b04184fa250bd7ff08fab48': 'in the sweet, flower-stinking streets. He\'d',
'ddd28bb5c57463115d9f5f2b453d4c01a1f87754753ac1b5871e3232fa8d488c': 'cense is invalid or unenf',
'df08c98f7ec2c0829a72c39a960b940eb38f5fb5dce49e4cc1e4381802dcb0ac': ' trying to die',
'e5ded8b924182a25ee05ab088dab1a079fc90623ffb1412f7c0fd80b2b9da7cc': 'ork. * Any of these condi',
'e617bdf5a56b7a69c240811b14d275b66f57520ae7debf7c82174af8737f346e': 'runabout. # Some peo',
'e71f4eb6142e71b2e3a40a7549ad450a769077abcc0c0ac14ab5ab1ba7b555e0': 'etulance. "You can back up that o',
'e7a94ffda46d4cd2e82edbbc7b1b216896e2f149f973800f543fe5d4f052c16b': 'LE LAW, AND EXCEPT FOR DAMAGES ARISI',
'e81af8a832a36f5d3c4895e2a0940be1e6ab1c2b4b4f1b5c18b8fba33fec011b': 'e. c. No term or provision of t?s Licen',
'e81f341a44daf879533a2024cf9d31c13660dad03346e5bcef01181a240e248f': 'Franklin streetmosphere players ',
'e885277f7c49e3e91a1b41a4f3e731c3e972055bf9daf089395a690b4d8da920': ' main gate, and turned, thinking',
'ea2dbbc99810940a61c46c23c666ae144f047d31450d2c0d5f030bd9f38e7967': 'mation, sciatica and slippe',
'ebd3a119b3cfc0378fdac262ba20b13241d1a62fb4b4ed9fe33b13724a3d75f3': 'ingdom and',
'f01620f1e22b257c857190f7a2311fb8b94418c19fc9c196106c4559f2d1e08b': 'le. "Hi there.',
'f1bc39392129fd051a786a66065c32d7835953cd56e5624a5f4fe2d89670c6c8': 'y have objected, but, hey, they all',
'f3dbecbf33816c234cbd660af108505609bbba520ca12d6fe3fca41577f865fc': '"Has anyone',
'f6af8e47cb4d790e2ab5fc601aba9c382a3a093d411c5496360719f7b8de5a12': 'd. "Late',
'f7145852e270e9948e1ad1c50bf62489c111f4fe172de9f922415f5c912b8b2b': '. "Can you meet me at the Tiki Room? It\'s pr',
'f899632346b3d1511540305659f4abde3499038a28a82967f96b2db78690f075': 'sob. "I\'m sure, doc." "All right then.',
'fb006a3028eb2be603847721a908f02e0aa5f4e8bd7b90059dd29b325a9d65db': 'inted a finger at me and, presumab',
'fb1ce23d6a664c60adce6be3229cad8a15fc8e10654cc810141ef4c29e9f1dc0': 't her, because',
'fb33e8130af0ff079485ae002e6be30a73c090d17d5d661618f51693f04a3ef0': 'reathing',
'fc15798394e39a49d85089d8f5207aa8113531fa3f6f7751c69d04a5c77a9bd8': 'ing me with one of our old fights,',
'fd5eb9540e65a1ea749a0b5c408f97282e5b4036cf16643ddcb8a754793d6747': 'ousand times -- in refere',
'fdfbaac6f478e138e5a42eb5a50cda1d05110496440d1dc8e0a78a5cc777b4f5': 'tutes a Col',
'fef2e6a8730be79141036f18fedbbd47c473345e651879bcb5790372faf2a5ba': 'st Abe, then fired h',
'ffd32615055580ceefda1df0fd92d59add984bd7ffc9fee422c3c9e07bdacf60': 'member costume, cut'
}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('cm2k-witchcraft_5f60e994e19a100de1dee736608d639f.quals.shallweplayaga.me', 12003)
sock.connect(server_address)

input = sock.recv(1024).strip().split('\n')[1]
print "File: ", input
answer = base64.b64encode(answers[input])
print "Answer: ", answer
sock.send(answer + '\n')

while True:
    input = sock.recv(1024).strip()
    
    if input.find('flag') != -1:
        print "FLAG: ", input
        exit(0)
        
    print "File: ", input
    answer = base64.b64encode(answers[input])
    print "Answer: ", answer
    
    sock.send(answer + '\n')