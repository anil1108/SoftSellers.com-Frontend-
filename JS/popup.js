'use strict';

function close_popup(){
    document.getElementById("pop_1").style.display="none";
}

function show_popup(){
    document.getElementById("pop_1").style.display="flex";
}




<nav class="navbar navbar-expand-lg p-0 bg-body-tertiary">
        <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button> -->
        <div class="img_container">
            <img src="/images/logo1.png" alt="not_set">
        </div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-span="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        <div class="searchbar">
            <!-- <input type="text" placeholder="Search.." id="t_search">
            <button type="submit" class="s_btn"><i class="fa fa-search"></i></button> -->

            <div id="wrapper1" class="wrapper collapse navbar-collapse">
                <div class="search-input">
                    <a href="" target="_blank" hidden></a>
                    <input type="text" onclick="addclass()" placeholder="Type to search.." id="t_search">
                    <div class="autocom-box">
                        <!-- here list are inserted from javascript -->
                    </div>
                    <div class="icon"><i class="fas fa-search"></i></div>
                </div>
            </div>

        </div>
        <button type="button" id="start-btn" class="mic"><i class="fa-sharp fa-solid fa-microphone"></i></button>
        <div class="collapse navbar-collapse">
            <ul class="items ">
                <li class="item"><a href="/homepage.html">Home</a></li>
                <li class="item"><a href="/login.html">Login/Signup</a></li>
                <li class="item"><a href="becomeA_Seller.html">Become a Seller</a></li>
                <li class="item"><a href="add_to_cart.html"><i class="fa-solid fa-cart-arrow-down"></i>Cart</a></li>
            </ul>
        </div>
        
    </nav>