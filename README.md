# Core Phylips CATS puzzle - "Turn Your Photos Into Bitcoin Private Keys/Addresses"

This puzzle came from Core Phylips [[1]](https://corey-lyle-phillips.medium.com/part-1-3-turn-your-photos-into-bitcoin-private-keys-addresses-57669771cf7a) who described a way of crypto (BTC specifically, but could be used anywhere) Private Key generation using any media file - like a photo of your grandma or your favorite song file from your Walkman. The general procedure is pretty easy and is described in details in his article (as well as in his github [[2]](https://github.com/coreyphillips/bitimage).

To lure ppl more into his idea, the author used a picture of cats used in the other stegonagraphy "experiment" before him [[3]](https://twitter.com/aantonop/status/603701870482300928). This picture is also presented below:

![Core Phylips CATS](https://github.com/HomelessPhD/CorePhylips_CATS/blob/0326d559cdb1e46c3a3720876091f71a8913c603/BruteCats/cats_2.jpeg)

He used this picture with no password (password equal to nothing == "") to produce the BTC Private Key and had stored small amount of BTCs on that - address for that (p2wpkh address, pay attention) is ["bc1q57euh23y3qs2f9d5mtwpax5lqecfvrdkqce82a"](https://www.blockchain.com/explorer/addresses/btc/bc1q57euh23y3qs2f9d5mtwpax5lqecfvrdkqce82a) and it was drained imidiately. 

BUT, to get the ppl interest and probably to prove that this system is still safe from attackers, he made the second Private Key - WITH SOME PASSWORD. Address for that (p2wpkh address, pay attention) is ["bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r"](https://www.blockchain.com/explorer/addresses/btc/bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r) and the funds are still there - 0.01 BTC.

He allows us to drain both "wallets" so far, the only thing we need to do is guess the correct password. To try your guess, the author has composed a website that uses your picture and password to produce the BTC address using JavaScript [[5]](https://coreyphillips.github.io/). AND, at first, i was about to utilize this site through extra JavaScript injection or so, but it seems to slow and so i've composed simple Python script to brute this password. The script "brute_cats.py" can be found here on github in the folder "BruteCats". It uses the cats_2.jpeg" image and "pass_list.txt" file. Going through "pass_list.txt" line-by-line it tries every line as a password and, in case, if it gives the requested p2wpkh address it will store the password and extra information in found.txt file terminating the script work.

Well, that's actually all the important information i could specify about this "puzzle". I have not found any clues or hints, but I tried 1/3 of rockyou.txt pass list along with some composed from his article\github word passphrases - nothing worked for me so far.

To run the bruteforce attack on this puzzle:

1]  ***download*** the ***"BruteCats"*** folder (clone it, download the zip with it, whatever)
  
2]  ***install the python*** and all required python ***modules (hashlib, bip39, bip32, buidl, codecs)***

3]  ***fill the "pass_list.txt"*** file with the passwords you want to try

4]  ***run*** the python script (***brute_cats.py***)


## P.S.

Thank you for spending time on my notes, i hope it was not totally useless and you've found something interesting. 

Any ideas\questions or propositions you may send to generalizatorSUB@gmail.com - also look at my twitter @MiningPredict.

-------------------------------------------------------------------------
### References:

[1] Core Phylips original article tells about the whole idea AND the "puzzle" itself - https://corey-lyle-phillips.medium.com/part-1-3-turn-your-photos-into-bitcoin-private-keys-addresses-57669771cf7a

[2] The BitImage project - https://github.com/coreyphillips/bitimage

[3] The first Private Key BTC address (drained) - https://www.blockchain.com/explorer/addresses/btc/bc1q57euh23y3qs2f9d5mtwpax5lqecfvrdkqce82a

[4] The second Private Key BTC address (NOT DRAINED yet) - https://www.blockchain.com/explorer/addresses/btc/bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r

[5] BitImage site for "slow" puzzle brute or other keys generation.... - https://coreyphillips.github.io/

[*] MiningPredict (my twitter page) - https://twitter.com/miningpredict



-------------------------------------------------------------------------
### Support
I am poor Ukrainian student that will really appreciate any donations.
I have no home (flat\appartment), live in the dorm (refugee shelter).
 
P.S. Successfully evacuated from occupied regions of Ukraine.

**BTC**:  `1QKjnfVsTT1KXzHgAFUbTy3QbJ2Hgy96WU`

**LTC**:  `LNQopZ7ozXPQtWpCPrS4mGGYRaE8iaj3BE`

**DOGE**: `DQvfzvVyb4tnBpkd3DRUfbwJjgPSjadDTb`

 **BSV**: `1E56gGQ1rYG4kkRo5qPLMK7PHcpVYj15Pv`

**AR**: `0UM6uoLrrnxXuYpHMBDAv-6txNTMdaEkR2m_bP_1HyE`
(have never used Arweave wallet)
