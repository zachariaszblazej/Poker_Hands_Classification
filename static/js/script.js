var s1 = document.querySelector('#S1');
var c1 = document.querySelector('#C1');
var card_1 = document.querySelector('#card_1')

c1.addEventListener('change', cards);
s1.addEventListener('change', cards);

function cards() {
    var suit_1 = s1.value;
    var suit_1_changed = String(suit_1)

    var rank_1 = c1.value;
    var rank_1_changed = String(rank_1);
    card_1.src = `static/cards/${suit_1_changed}_${rank_1_changed}.png`;

}


var s2 = document.querySelector('#S2');
var c2 = document.querySelector('#C2');
var card_2 = document.querySelector('#card_2')

c2.addEventListener('change', card_two);
s2.addEventListener('change', card_two);

function card_two() {
    var suit_2 = s2.value;
    var suit_2_changed = String(suit_2)

    var rank_2 = c2.value;
    var rank_2_changed = String(rank_2);
    card_2.src = `static/cards/${suit_2_changed}_${rank_2_changed}.png`;

}


var s3 = document.querySelector('#S3');
var c3 = document.querySelector('#C3');
var card_3 = document.querySelector('#card_3')

c3.addEventListener('change', card_three);
s3.addEventListener('change', card_three);

function card_three() {
    var suit_3 = s3.value;
    var suit_3_changed = String(suit_3)

    var rank_3 = c3.value;
    var rank_3_changed = String(rank_3);
    card_3.src = `static/cards/${suit_3_changed}_${rank_3_changed}.png`;

}


var s4 = document.querySelector('#S4');
var c4 = document.querySelector('#C4');
var card_4 = document.querySelector('#card_4')

s4.addEventListener('change', card_four);
c4.addEventListener('change', card_four);

function card_four() {
    var suit_4 = s4.value;
    var suit_4_changed = String(suit_4)

    var rank_4 = c4.value;
    var rank_4_changed = String(rank_4);
    card_4.src = `static/cards/${suit_4_changed}_${rank_4_changed}.png`;

}


var s5 = document.querySelector('#S5');
var c5 = document.querySelector('#C5');
var card_5 = document.querySelector('#card_5')

c5.addEventListener('change', card_five);
s5.addEventListener('change', card_five);

function card_five() {
    var suit_5 = s5.value;
    var suit_5_changed = String(suit_5)

    var rank_5 = c5.value;
    var rank_5_changed = String(rank_5);
    card_5.src = `static/cards/${suit_5_changed}_${rank_5_changed}.png`;

}


