---
layout: null
excluded_in_search: true
---

// https://codepen.io/yoannhel/pen/sJvcF
// Thank you!
$(document).ready( function() {
  var header = "<div class='icons'><span class='entypo-cancel-circled close'></span><span class='entypo-book-open open'></span></div>";
  var margFlap = parseInt($('.flap').css('width')) + parseInt($('.flap').css('padding-right')) + parseInt($('.flap').css('padding-left'));
  var margLarg = $('.larg').width();
  $('.larg').css('max-width',margLarg);
  $('.flap').css({
    'height':$(window).height(),
    'margin-right':-margFlap
  });
  
  var i = 1;
  var color = 0;
  function countColor() {
    console.log(i);
    color = (i % 2 == 0) ? '#303030':'#3d3d3d';
    i++;
  };
  
  $('body').on('click','dl dt', function(){
    countColor();
    $('.larg').animate({
      'max-width':margLarg - margFlap
    },600); 
    var word = $(this).html();
    var dfn = $(this).data('dfn');
    var wordurl = $(this).data('url');
    var html = header + "<br class='clear' />";
    html += "<h3>"+word+"</h3>";
    html += '<p>'+dfn+'</p>';
    if (wordurl != "") {
        html += '<a href="{{ site.url }}{{ site.baseurl }}/term/?q='+word+'">link</a>';
    }
   
    if (i != 1){
      $('.flap').eq(0).after(
        "<div class='flap' style='margin-right:"+(-margFlap)+"px; background-color:"+color+";'></div>"
      );
      $('.flap').eq(1).html(html).animate({
        'margin-right':0
      },600, function(){
        $('.flap').eq(0).remove();
        $('.icons').animate({
          top:0
        },700);
      });
    }
    else {
      $('.flap').html(html).animate({
        'margin-right':0
      },600);
    }
  });
  
  $('body').on('click','.close', function(){
    countColor();
    $('.flap').animate({
      'margin-right':-margFlap
    },600);
  });
  
  $('body').on('click','.open', function(){
    countColor();
    var count = $('dl dt').length;
    
    var html = "<div class='flap' style='margin-right:"+(-margFlap)+"px; background-color:"+color+"';>";
    html += header + "<div class='list'><h3>Terms</h3>";
    for (i=0; i< count; i++) {
      var word = $('dl dt').eq(i).html();
      var dfn = $('dl dt').eq(i).data('dfn');
      html += "<span style='font-size:12px' data-dfn='"+dfn+"'>"+word+"</span>";
    }
    html += "</div></div>";
    $('.flap').eq(0).after(html);    
    $('.flap').eq(1).animate({
      'margin-right':0
    },600, function(){
      $('.flap').eq(0).remove();
    });
  });
  
  $('body').on('click','.list span', function(){
    countColor();
    var word = $(this).html();
    var dfn = $(this).data('dfn');
    
    var html = header + "<br class='clear' />";
    html += "<h3>"+word+"</h3>";
    html += '<p>'+dfn+'</p>';
 
    $('.flap').eq(0).after(
      "<div class='flap' style='margin-right:"+(-margFlap)+"px; background-color:"+color+";'></div>"
    );
    $('.flap').eq(1).html(html).animate({
      'margin-right':0
    },600, function(){
      $('.flap').eq(0).remove();
      $('.icons').animate({
        top:0
      },700);
    });
  });
});
