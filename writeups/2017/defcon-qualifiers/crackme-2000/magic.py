import socket
import sys
import base64

answers = {
'01dd90c3b7d9a36227a5ddc96c7887acbcb973744c1971eaa6da6cccc6c3e261': '==== The meds helped ',
'035202082a8be265d23b0409bec1d7c080e1ee14c163874f3321b6c70a209a7c': 't of respect for',
'04818b31ff02ad50af2b052c3488b13b8be29da3c294857b8b159a3df5df6139': ', turning me int',
'0626de9df535695be1dc8817e2658d1a154ef4a49d146ccf0cf5bdbc4cf8dc9a': ' turn it ',
'063e89efc6c79782ed13d165f6af7dcd3976a156a5e78ce653a79b990f234859': ' opinion. I could find you somewh',
'06d2e3d6567f6838dc12dcb010b0965520533703b2274698b657e3cf669bf31d': 'y of, or the',
'07762aa6cbded2e2328e952b78f1aaa7e7016378403210534c6aa27a0c4d0999': 'hinese pirate queen, which was credited with re',
'0af4913433ca0adc86ad2befd7ffe465239953364a8e1dcfbddbe05254bb8c25': 'de. On the last night, he presented me with a ',
'0c029d126ab043c1b5137f8ddece16af67857743cc1a8e0d496181f002861c04': 'han anyone -- shir',
'0ce972b0c62e2ead09545327441937e2dd60c576b33ee04d80c3003b4c6672d7': 'arket at the time. No one wanted to s',
'0cf5c1b760776e29681630181ba77cddd4e424844e900ed697a97687bef36a51': 'e and I\'m a happy man. Now, are you nuts? Pr',
'106e82501d48692b7cdcc75be9333c5fbf32af8ac7eaff2b184012a4978f6021': 'he word f',
'1381ab9c33d6f6471879dc859df2082231a739f30918b192fb590d4903ae2805': 'd a relieved sigh and smi',
'13d198223ee4c757aad8d411f5a9526d6bb13cfaabf3c01394d2e1a84b9ffbc2': ' morning and drove to the Magic Kingdom\'s castm',
'14db6cffc92b0169ae806eb8b15eeee20c16f6711dcc946451e0cb2ceaa12e67': 'the era of the cure ',
'16f5b4ea60305956a7fb18b917e6a9f8ad790daf4d27b48f4ca70d6cd75972b2': 'ith would have to answer their longing',
'18ac383fe75186fb788d030854e6f7ce6d483b50aa728a41001fa56496763c16': '. I got into my runabout and Dan',
'1b697a15230868c9701182b5c9f5246b1dfea3ee68cac7d966e76830538cb2f0': ' subvocalized, "lo',
'1c04d682e0989856343ce1d48fe92d2c672a27136dbd6f0cc280a581300c260c': 'm proud to be ',
'2011437c41dfd65616beecace1361e7603768f6227661eb3454fe7bd74d16554': 'ra\'s people had stashed there, alon',
'20ca4b38a044b8a61068b90b9333736a9ec38390597a7cb3da1ff28d9ad67112': ' Park a century before',
'2279440b2a941d316753a3ace54fd210304dc8a9f37d2f430eef804552aeade8': ' guests along with it, dancing',
'230d5e7c4ac8a9f1a39e361982932b60b5be0ae032192c25e18ec942de3b5ca5': '. For t',
'241314e79b9254fe476c23b18bbcac0cb4d53dc0c4aab10f3f7d2e30f88ea896': 'ha, but I think I\'ll do it t',
'28a4f8a23587d1919639ff4114e18c7653ddfff4d338f88247820ac61dd1ef54': 'ut of a printe',
'2da93111b53b20e8588b6291b842593c6d0e04686c0a15ed8abbcc7c756ae02f': 'le place left on-world that isn\'t',
'2dfe26b405da3843de6d6d027fd9efa12e4253607f2241b5e59f5a07af5fc0ef': ' even a modest shoulder',
'2e897c529e13f8afa21f2da97d465b292a3d3dbf2e05902eb1c1aab8febd7aa6': 'ail. She took my hand and kissed t',
'2ee6120c5e209cf239c8fe389c1bcd21160581437bfe0c328377ef24352c48e1': 'hrapnel. I saw the girl\'s sm',
'323da730235582b75113790bd7b50c1803386416ebdd45e5ece14c2394f8720c': 'push it out',
'342f92e7e3bfa6995cf14501c97463cada57af6480d5f77dd09cd4e07cf0ba3c': ' a prototype for that afte',
'36221aba23a542f95251f06f33ecb38ccd00e24e47e85a7007e291e4422d64c9': 'de for petulance.',
'388d1b566409a9510ff6f6c729fe28ddad25a3f43090e79349be7a22f7bc09fc': ' that this project wouldn\'t c',
'38a3d8f7000ad84ecc5806dbe98fc9faf6d326f4e8195162193968a9aaf5ae51': 'Pleasure Island to your public d',
'3bd67d2544d15341c4e50101df81fdc4584040c6ded0b1c02ae0168c362b2d6a': 'kitchen and got some tissue,',
'3d5804a4fdc960b35518f87309f75f1a0703ab6e5e4bb1f0efa3666d8503d168': '=========== Other book',
'3e96a8a9c4f1d6f5b9478e3efff1787d1d49fb086df4a61d901cc4407ae4a13e': 'nd catch ',
'3fd8e067af6a7164f64451916885b11b9f909ad18d189575373f17becbc0da81': 'ence between _you_ and an exact copy of you, is',
'3fdd6c9f102fb6bac3736d94d361bb4151f1d39ee88b06de82961018ba2773ad': ' a baby. # Of course, I got caught. I do',
'40b79f3f33c52666b495999bbe8c26535f8b99f914dc943c7921b0f898747cbf': 'rbit, wh',
'41ddf5930f2c9bcf4ae923b5db99b8c732f55af563bfa7271a34562f6d62e0aa': 'ation, fictionalization, motion pic',
'4245f48054debd4d1a4cc0e5bd704705bff1440607443b8c6fc5c342d067e93e': 'ike a monkey, the living quarters and b',
'4364dfcfd9d5dae1a81c573676f0f7bae2c8bcd4397cea316afa0f1cbc6bde91': 'n. Please?" He sighed in undoctor',
'4502f48672674d423632a780f074c1a6faf3e8141a6da5ce79308be7fc4e59c9': 'crews scurrying i',
'4602f6308447f7720b0015c43875c9dd1952fdfcde9d1df5d079e700b4992d04': 're in her',
'47f8bc7df433c62df0788660a32dd83ac03938a9d7a627abec3a40b1c012f7eb': '-- the blood-temp sal',
'4862c952dfb9b310baba444dbbde64aab63c92c27ad9b11b4bc401c4c35a5dda': 'uccessful go of it. So it fel',
'49821bf5a649d59d592d63924d9a42298c305da3903d8537b3d7994b3e3bb812': 'own the staircase, f',
'4af5970f00b220a7a24c77a5eddd2116755bd2c20f77091a00cd0bf2f0db39c4': 'met in orbit, where I\'d gone to experience the ',
'4b30cd407458a11f1cbcb433ac0bfd151ea26ecc871b5a4fc5a21f3fd4055fb8': 'bliterated a',
'4b8b59a189feb5bce4dc4d43d79badf09f2ac1411721343a41260b7458d31b87': 'g the name (or pse',
'4b9aec86be530019000b30a67a32870a39f2e1fffd449e055e028fe9483d77bb': 'd, thinking I\'d outrun Lil and Debra and all',
'4ba7477cc1cdf90ddfc5e72142a4dfed4340d460043d813eec7a227be96291b8': 'or support. They looke',
'4bc2b449b1eee41b4a50039adcc6ca453aad7396eb387f2371ed9d6a982ea68f': 'arted to boil in earnest. I slammed Dan\'',
'4d2ba4b8cf958d99109c9e19344cccb0bc3f11d1a2e805afaa2b8656fde98225': 'ur succe',
'4f49c8c63601a71d3ae23694f78951fd3c63ae9ce295e92cfe67378cb2c7e22f': 'ould make more popular ',
'4fba88cdc091cfbaee1399db369c8e43c44ba797ea64fff5bb813df4e8ebd1f3': 'w that I',
'5020e97f88e8b58e1aee18ddc4bcaa05fc47b6a03ee2956e459613c86b41d089': '. They must',
'5189e2992ea3ece0ba99a74c10c311132305410d381dda6cdb9f5c36d42166e9': ' they had, and I was glad. It',
'537a4d4f4c54d4838a6a9cb98840ac5a6bdc0b2f8c30c28e13a69f1bff80607f': 'ula into a cookie-cutter, st',
'550d4a3c0add395524dabaa290929a040dadafb3f54740575e3cf43ea8dfddb3': ' and the house w',
'574b243ac620392d899fb47bfad496633d061aa404013097435625800da3b163': '\'m concerned, we are on the same ',
'5828f04ee8fa1a1906c013bebcada8af965c7efaeef2c73b2b1a3477b1089be6': 'r me, thanks! But camara',
'5adb6ed0486b8b8fd1142a5c5617a39b8b99120351be91b3c28afebb026ce031': 'She had no way of knowing if ',
'5b0490ea26d5548596ca99c3f9592c5d16228a6ddeab3aa45a0dc7fabc14ca20': 'fore I collapsed against a wall, head down. ',
'5cd47c03c44ab6e407cc48a3ed0244d97e9a0cecc631ee981dad363845e73cfa': ', common law rights o',
'5ec7cf09a1f1939f0481ffe9fb9196abb01ff186c22112ceea2d55e320497367': 'e me, I\'m just as ups',
'6042950812bf5207bebe3ac14be580595af67cd5e75da0549dc0ee21f4dbe9d6': 'all my problems. I\'d thought wro',
'60db3260a73ad9d2b5c376faebbd71a1a3cce271467df2ec74b5d154576ab5cb': ' "My Whuffie\'s doing g',
'61af7fa8213889badda3b121b251f4e796d54215c8b5b3085cdeb57bdaf54db4': 'there. Wordlessly, Tom hef',
'633b4397b1d891b6a83feb886d2dca30f267ed8e6bb7f1cd4776db77442d7a80': 'lus, a little paunchy and stubb',
'6357d72bbc7c5bdc18d78b722da62e7802a5a5d15b5935151474eb8e7ba80fef': 'l and I had come he',
'63c2cb0b02195932af1f88a86d27cca7ad389e7680739e43d97f60e7d69ebeb8': 'age in the process and losing my nerve, tell',
'645860c48ac0e65bf1b3eaf6ffb45c138800a2de9876afd9bf856b1a54ccb4fa': 'y footprints in the Contemporary\'s lo',
'65cb596908789372c2d6fbeb0ac3a0e3a1089039138711a016ec3994ad5c7f10': 'ouses in their hometowns. The Mansion\'s better ',
'6647d6a568030314a08b14db08d18142d4c4db4fc715309caa0868d65c8a59ba': 'e was incrementing u',
'679f3eae9568c0003e6238fdeddf63079446657e44dd7d67a13dd4ffcf644021': 'o the fried-food-and-disinfectant p',
'69651a40a2056797235a2c05f44067a419fefc53ee1fc363587da484c90cf3a2': 'ay have been te',
'6ada437e8ed5961ba02867b18aa6f15b2778b472ee156f908c867e3236d66821': ' and several of them were watching intently a',
'6d864d6ba2cbd015ffa752f3cf01cdf2b30116a5b5303169f5f310d97230b134': ' the Work under different license terms or to ',
'6f0192aba03ee052a29849607a1b58405cfd6d6d07a4a2c012c64682d9fed0a7': 'c, sci-fi prophecy on',
'71e95588b183b5ad9527f1857679f3343b9e61573a5e51292ac2e8c0284d3aef': 'stmembers to help them out.',
'71fe4a85acfd3f68031cde02ed636905027b66ade35a30badec10da3475786cc': ' Haunted Mansion, if you just give m',
'733c651ebc91e8b92df0436ecc5234121208b669665af7722efcd04eeda3566a': 'der. "Thanks."',
'77047a6f88617ca1da4be41a139b714527fa37bf03ee73d68ae4c75de57ae543': 'he beating on the 88 like they were',
'78c85eae977a1fcf84fd48501613ef586928466de334d02ee820b1126da78af5': 'side. Th',
'7ac69cd13ebe95412e0b09d7ff3519520b0f07fc879263119ad448fdffd337d3': 'storical preserve, Julius, it\'s a ride. ',
'7d373be21775bd17a0274f5ce4942c226fde35681a94cbfd202409d4fb1214f5': ' the Hitchhi',
'80e0b7863a7e12f74d65deb3a74a1b75fb089b0889a81435c9a6ceaa5440cf83': 'l -- I had no way of answerin',
'8199f850ce0ce31b7645833e23860fc4beb307da1b2f3a3d657712099e39cd92': ', on my eyes. I opened my mouth and inhaled de',
'81cd673b9a2977245493e7004015878892d69aba7eeb38c1002ab85a1d374462': 'ale or other limitations on the exclusive righ',
'8241af0b4cfe07e3974070251f074ffd62a0e32e22ecb973a1c4d6381e39097a': 's good a guide to th',
'84e0316e72def8de349f3cd5b8fa8f23aca9595bba21d2c99103f0a88bd3419e': '. "Look, you don\'t have to roll over for De',
'8609728e104ccac3d5b6d0294ac8b3220cc068e5d9c4857a125b9cabdaa82bf1': 'ind as I staggered into the kitchen, where Lil ',
'86719d3c71e770087e259b2b9366b1de756bded99a898075a0cf4809ad8c2248': 'of armor, he could _improvise_. You\'d get a sl',
'8709c3008229b4a85ae46db0a06ce7e40b1577c7f617665fc94996fe8d50bec6': ' believe',
'89b87dd3c7337ee08fa2328fedd2f46b0aa01aab7c8ab972555ec067f976dab4': ' copyright law or other applic',
'8a11a9d80bb3a6c7acd51648fee16d759fb378ecca860bb022f8b216ca6ce70d': 'rd anyon',
'8d4cc14bcb1ce3778478bac082ab47168c2d89281728e73022e0ec35f959f74e': ' and to concentrate on Dan I had to tear my e',
'8e1a91edb30ee168ba685c79f0b860413ec18c69d396066ce7a29f8c88f52f99': 'd all rights in ',
'8e5fe9d2078e7776c9b22db96420ec82c067b714e144a218f0f53d96a31f0460': '-lit corp',
'8f714ab38480e0b4736134043bb243ce9c6d2fdf1108dfed4cc2e1f9ca831b92': 'ehind your ',
'90ed7942efd811bbc6e9ab0daed447a3ec184ed7ad2c5ee619f836a149b8c8ac': 'org/cc/Share',
'91d1b6050543c9054b122c0b78ffd15a1665bb21d2b7b29b1871e3192314d2a0': 'd a moment l',
'922b45b102fb8f5af419c03c4966fe6b10f1b93e0b51ee794dd88c680713eb24': ' had to remember to call him Tim',
'92bae9e12d0d4c1af32166865e1b585d4a66c27012261151a3582e859dfd2814': 'e, and he was takin',
'93f8dc77a715e11cd4f9899b5833a60739c3046c2e3f3826785ee9bc20b8e032': ' with re',
'9541279759fa881969e154b6f093836342c007848151074b4aa44adc9b3ac1b3': 'der this License who has not previous',
'9a12cd39d75a35322c3cf769418fcac2f8cefbb59403a9b82d25aa8fddd84e55': 'en gave up and looked at Lil',
'9b1823ae838e00d19fa93d95f8e6c0b02dd499294a894cecf49c4b403da10a31': 'iverse gets older. S',
'9c5f26f865a223eef364f22636df19fef4db269711d125d2dfd782f36779cff0': 'Julius --" ',
'9c7ba79379454912b670bad275be397d6e602939d0ab99ff217585b05e919422': ' of the fire',
'9c82009563de70ee6bfe44426b963df25f86f324dc12b01a2eabde6c1c20b1b4': ' full of other bouncing, happy',
'9ebe31abe7eed2ff891ef8ab10d915fd06906ac0c0c3c698bfef8e2321b1a0d1': 'eep was ready to kill someone, I s',
'9f24734d3d96a3ca42f5fc404f3a717dabdab8dedd8eed32da08db3ad91cb050': 'he _best_ work ove',
'9faa9c35e93d785f3511887ba8d0878d4e1d8bfa420a2cdfd8dd009db31375a8': 'led at my ',
'a0ee8883fadf9cc700dd50d84392ecd03a55203a6e51242938401ad4e45d376c': 't." "Can it wait for ',
'a181945d3f4003f306bfd5ac7414d458737e2d362671e6e6addb82f8bb65832d': '" he said, "for the moment, that Debra r',
'a1b10665682489a4c5a388c26a75ab50194574942cf48058bf948f8a100ae24d': 'ouldn\'t be good. "Yes?" I sai',
'a210dea1a1b877ad178d1718c2ccb1fd5e5e0484eeb907e05dbcca2a07ee0e85': 'gone. A quick chec',
'a25cf7d89fb7f09990522165222d51d4385cdab02c6b137ea15b782f837353f9': 'unmuffled,',
'a3870f5b1773abbe0c35325f1720d6124bd7024950341f376c2dd22cdca9acb0': 'ed to talk to Kim. She was a problem I di',
'a4313f2a638517213a6f3c8d47a66e51672610801793bde4ff447bc8f83d8e14': 'was out, th',
'a736e21290fe5431a1aeb41f9df06f2d745e3a5232feef62589adb550ca5ad3b': 'igure out you are not. I have something t',
'a979bddda6064d842e3e62bb7f0ecf8331788c9c92a8c68719cad9c803af0397': ', and that was th',
'aa423fcf9e08fbd0ef59a5eef6a4a246c3fbbf31b6dd89a1f7abd7f6b27e2ff8': 'I\'m a sucker for musicians. We brought ',
'aa672619e0cb05d025b0b9bc9259411d4271859c8458c40f88c0d2fb390c80f4': 'I asked, hating the self-pity in ',
'abe60de564ff191f6a001dd43fb4285f74735498bc39c3df63d19bbb591cb01c': 'burned all his reputation capita',
'ac5058cd6b06cee176bb058e6e23d560cc4848821454b8f0d8ced4488c15abdf': ' needs Cory Doctorow! Br',
'ae7a151f4d61fd1c4418579058245398d8a2abbdce5801e8fd822664db733669': 'her in -- you manage ',
'ae9466bd227a8faf195eea1f0d6f7ecd535e641af1cb04f0ce1d4ad58fcd2cbb': ' old Cheyenn',
'b5a7cee1b935a4c09bfb40954da1a1cc023e48dd9906bb5f100686a112b1a01b': 'ince I was',
'b6185317625d8bec0ae7c422fb022d71dc0053899f30b7e7525db8b14f5bd498': 'lidors and then put it on ',
'b6d7ff0e83f6ac0ac741bc2c64b5b46dc2a274dd83db63c5e41c36133ac1be43': 'tive work under terms',
'b6f4d63cb7d8d732b28223eaafee8c4025d7d1159fc9b09f7587b6346d43b588': 'o the Doom Buggies, shaving 25 seconds off the ',
'b8fac4455f255f0b41426d146ff931ed6329ebb29f41092e4bbf07fdf6c50fb0': ' parents went into their jars with ',
'b988d66d641b05eb1ce55166af6b028ab7fa6c060c0e7474b71662e17159964d': 'at can I do for you?" Under the veneer of',
'b9b056f257d7cc013d1910b70c91f5134c209b1219f950cabe9715b99fbef9c0': 'treet infirmary wa',
'bbe770ceb3dd296e2f10c7582a287e28026ad31fc721c82e3314b9c79a2395e5': '. No hard feelings." I stopped',
'bc5b48bad58b5720eab0f1668aa4d255a7ffd518340031bdc5b3e1a49ad75dcf': 'y, reason trickled back into m',
'bc90d02659b1d32bcb78031f85b72cef4d8f48ec55abdd350d93e6268959c1ce': 'and was about',
'bde768e64d839338e587109260544a1810ef4d238a60e2e30587cf9481f2cf7b': ', one way or another. The discussion we',
'be0d8894e8e55488006b66221f168a894a9adb2a88d22fecf2387d9cf7ce8edb': 'to a half-a',
'be422c4d780fcc9f29d01283ad76088529af9b4dc7a69c3bb9979fb51a23824e': 'ed coffee in the general dir',
'be47da219e225e5c9ff7dad4c3fa450f6c9febadbf9734053921779e02ce71c9': 'ividuals. In the years since, I\'d lost that re',
'bf80857755515afc689158cd0dc6c47376108a2a00d496439d9633149f48ce0e': 'tle, across the lagoon, I cou',
'c00b7fd5118f32053eec653843bf02b26389aff2e63941a1688e4b93d84343f6': ' head rested on Tom\'s lap, her fee',
'c0d5312126c2a52cb23f91694a22ba32284e59336fb5176ed92dc1cd23b62655': ' "I\'m goin',
'c187978c4de87eca2e3c898935c73926ce5d1a3a8af82a7b4fed46ec28701ff3': 'huffie up while she was evicting ',
'c284502f71e7b22193296bb3e37c8c16acc59fb3d9c26bb4c7ec32e08239d55a': 'as forgiven, but she bought in, and ',
'c341a4a61c43792e4ba0c6ac61a485a2435a138eb0ecb958e6b5f7f80792a678': 'odded and drank. "I thought it might be ',
'c3b8f92a1d7397943e03250c108143038c56e6e085cfc006fab4e32ef25a6a41': 'asonable to the medium or',
'c49b2bad92bbcc28d06b2461a50373e3f20282d5fc5b52dccb6910ee3c9e10ca': ', was cocking an eyebrow at her an',
'c6259ca6d19d11bed9c851d1e93a1b3b388deeadc332b9206b6a803b514480a0': 'he farthest one, beating my ferrymates to what',
'c9ccf357eed88f74bac5a31c924d7d7f2b63d98067c292bbd10cf935b537e3eb': ' thesis. I cut rapidly through the lu',
'cb18a603e6e5e46456ca704b204aa65475540dad6e64392bd2090d38b65695ab': ' the bleeding edge ',
'cb608f51e389ba73f2f76471d697360dacd3872cec1caab51937b50eaafdc103': 'lightless tube my only ind',
'cb65c85e9d6d3efffd23e1580510bb6f45b2ff8c05c84b9e8e377d3c03ffb34d': 'n a twinkl',
'cbc1c1bcaf66c7f95c5241899c1cb2b56b5ebf04253cf5dc8d1a5d04ad68343e': 'ts from the Hall, forgotten on ',
'cbd2b33147fe34316cc7e02ceff4e5470fad293395ffc204ab0646eb0857c3c4': 'd my skin.',
'cd9c54acfc3e2e88c9599b445834ff4697a31f620657928d11ed5abf29bedb0d': ' any part of." "So deadhead for ',
'd0305cda8680a28299e561928b49a796bcaa861bf7da013b8d0ce89b9fbac251': ' first time we\'ve disagreed. S',
'd04a08eb2023e447a57cdd1ef5aed043accadd5c2adb62b857d1005d6d8f11e0': ' new recr',
'd19be642c633fe8f44f3293503765437cddef2639279a2541ae3b996191dc38b': 'ded reluctantly. ',
'd4273bce80bb481da90893d27d7029f7c4dcd632c8e77f5f2e0cfcba512d5fdc': 'resolved not to speak again until the me',
'd7103584c2bc693a2f766c7fe59a255ee78af8f9b2e5ebb34b937966815752db': 'nute detail, bossing a cr',
'dbe69c930111372255a86942e9b8c7c9b76cbd349e689c41c4894a7f04c77197': 'make of. He looked a',
'df8490934808f5a02d8a39f4348d96cfcca0b57219a71f38d9fea0ad7eb75060': 'that changed almost daily. The newcomer/',
'dfa98e021a4521c4e548bf542b7fd3eea1d3d8c6361e1c8fde5394526f5d14ed': 'btle attention directed at the new s',
'e005a1973167b4cf47100c81bca178b98646a128e05a6beb804226888be3f344': 'doctor came in, shaking his head. "Wel',
'e17c6de87ec53223013eeffca686b2a75de4d08378ccde3fb1beba5f17641176': ' when it ',
'e30ddf599f6dfc8da98c4bbfa3d4beaa16d6a9c398be9beaacdd70a97bf35d4e': 'lked about it, instead of mak',
'e3f6d230246d578993756c30a1e7109836bb06337b8906242dbaea282e0badc5': ' by magical, dark',
'e59bfb77ecfb1ce040886c8c0c7169ec660eb261dc5a280b3fbc1af31cb05f92': 'Our little ranc',
'e5a0e5cfae3cc768d423348b809fbf1fbf86be376cd844f16340dfa2f3f5e1d8': 'bloodstream. "There, there," he ',
'e8e8d97445d62c249ea2ef5f254bc2a59735bb45380542786bdeb7ddd1f1bea5': 'ind as I staggered into the kitchen, w',
'eaa9fe704b276ef17a23f8cff65f32867370511adce25e00100e9e6677a5feb3': 'nt their tim',
'ebd3afc491548ed9b6589660e9c41834b7a6e34a92e6c2dcbe4cc392560b8d44': 'e to start over again. I knew ',
'ec934bcf42058cfbc2b239d26e835e390fecf71181fd6ae97815e93f233dfef2': 'xt" /> <license rdf:resource="http://creativ',
'ed6b12de149ad6f8a59b774ad1a825ec266611dd9b934d37a5303c93d49d1443': 'I fall in love. . . And ',
'ed75f72d1c4347f13b1fce3adec54ee47feb43a66d3356e01386e7807dfd6f62': 'Faraday cage and the lab und',
'eec7e5bee0b68da5e2d1e2f8cf09c04e40077219d0b1ed560db847a348b8fa8d': 'now how t',
'eef18eb6b320b7dd20c0a28f148a688fa17caf38ce9eaf5d45d4603731756329': 'cial advantage or private mon',
'ef1c8af29a2d46c12b3581f7157e712a1f5a943779e37d56930a5dcde30d66e7': 'ail. Even now, the Epcot ad-hocs w',
'ef9ea7d5c9fbbf10e16f8488e433b55672b523b64bc7bdea266e8347560b920f': 'atted my hand. "Strange ti',
'f03e215efd8dc8289e375615d59331a5f77e3b69947397b7fe6ed11318960413': 'make such modifications as are ',
'f0ace9ac47f1f37cb02f6d82a2c073b82373f2c9992860401457f336ead5d94b': 'afternoon getting tin-plated and iron-lunged',
'f14fd383ed7fa9d908a46a0b78ec21f793e5509cedaf78d41f060f54a61d769d': 't. I have a backup in ',
'f1e56ab8dc43fd0e33b79affdb5ac47911206c9a05f82715dbd7882c85fffd59': 'didn\'t surprise Tom, though',
'f3f396143f8d1cdfea05709d485f7275c3b7f948d019c088010c9968a54bae7c': 'ork into one or more Collec',
'f884d38b2d48aa374f19b455c6eb102749b8554e8cafc869b918f9fcfebadd02': 'ulate them." As I took her hand, I',
'f896e92246ad9364eaaed9a6d5cdef4f0f3966a5fa63008d5dc77bacab1ba8ef': 'away. "Debra proposed it. We were talking ',
'f96c1a402d0757f8b07baef25c806774be614fb9b7271172655e1195d37852f7': ' immediate',
'faf383fcaaf39fa4bd50598f41a2e5a4fae2101c20817df10b6c019915d2315d': ', it receded, leavin',
'fb63fb05c2ac38e1eb0b91ab1f1a0de18ade212d17dedfcad5b83bbe442fd086': ' to stop him. I needed sleep',
'fbb4fe36acdaeffb925ac04700f4b7307ff3a49522d455adec94142aff4857fe': 'es of the work -- not derivati',
'fd083c59ba8a162b1291d664f40c52a1da1d0cc658ba6c738c383025fbe8a999': 's, the process',
'fd091571c1c7889a43b4f829c563449b13103d7ad9f23ee4a2df507626c37000': 'ffie my H',
'fd9431be8119528acf27853559662473ae4f8a2cf7b2e1689fe9fb12943e9802': 'y rocked in their seats under the blast of',
'fecb014cab63df8b6a56da7a2edfe9ffbc3868579d445c4d4f0687b1583bc164': 'erienced this af'
}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('cm2k-magic_b46299df0752c152a8e0c5f0a9e5b8f0.quals.shallweplayaga.me', 12001)
sock.connect(server_address)

sock.recv(1024)
while True:
    input = sock.recv(1024).strip()
    
    if input.find('flag') != -1:
        print "FLAG: ", input
        exit(0)
        
    print "File: ", input
    answer = base64.b64encode(answers[input])
    print "Answer: ", answer
    
    sock.send(answer + '\n')