  let divcolor=document.getElementById('colorchange')
divcolor.addEventListener("mouseenter", function(e) {
    if(divcolor.style.backgroundColor=='turquoise'){
    divcolor.style.backgroundColor='black';
    }
    console.log("hello");
  });
  divcolor.addEventListener("mouseleave", function(e) {
    if(divcolor.style.backgroundColor='black'){
        divcolor.style.backgroundColor='turquoise';
    }
    console.log("hello1");
  });
