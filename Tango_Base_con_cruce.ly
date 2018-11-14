
%http://lilypond.org/doc/v2.19/Documentation/notation/graphic


#(define-markup-command (tango-pose layout props pose-string)
  (string?)
  #:properties ((thickness 1))
  "..documentation.."
  (let* ((th (* (ly:output-def-lookup layout 'line-thickness)
                thickness))
         
    (xoff 0)
    (yoff 8)
    (binc 45)
    (tuneth 0.5)
    (dur-off 1)
    (boxllx (- 0 xoff))
    (boxlly (- -1 yoff))
    (boxurx (- 12 xoff))
    (boxury (- 11 yoff))
    (boxurm (+ (* boxllx 0.5) (* boxurx 0.5)))
    (boxurv (+ (* boxllx 0.75) (* boxurx 0.25)))
    (laythick (* tuneth (ly:output-def-lookup layout 'line-thickness)))
    (boxth (* tuneth (ly:output-def-lookup layout 'line-thickness)))
    (dur-off-y 1)
    
    (llx (- (string->number (substring pose-string 3 4)) xoff)) 
    (lly (- (string->number (substring pose-string 4 5)) yoff)) 
    (llb (* binc (string->number (substring pose-string 5 6)))) 
    (llw (* laythick (string->number (substring pose-string 6 7)))) 
    
    (lrx (- (string->number (substring pose-string 11 12)) xoff)) 
    (lry (- (string->number (substring pose-string 12 13)) yoff)) 
    (lrb (* binc (string->number (substring pose-string 13 14)))) 
    (lrw (* laythick (string->number (substring pose-string 14 15)))) 

    (flx (- (string->number (substring pose-string 19 20)) xoff)) 
    (fly (- (string->number (substring pose-string 20 21)) yoff)) 
    (flb (* binc (string->number (substring pose-string 21 22)))) 
    (flw (* laythick (string->number (substring pose-string 22 23)))) 

    (frx (- (string->number (substring pose-string 27 28)) xoff)) 
    (fry (- (string->number (substring pose-string 28 29)) yoff)) 
    (frb (* binc (string->number (substring pose-string 29 30)))) 
    (frw (* laythick (string->number (substring pose-string 30 31)))) 

    (dur-string (substring pose-string 36 39))

   )
    (ly:stencil-add     
     
     (ly:stencil-translate
      (ly:stencil-rotate-absolute
       (ly:stencil-add 
	(make-line-stencil llw 0 -1 0 1)
	(make-line-stencil llw 0 1 -1 1)
        ) 
       llb 0 0
       )
      (cons llx lly)
     )

     (ly:stencil-translate
      (ly:stencil-rotate-absolute
       (ly:stencil-add 
	(make-line-stencil lrw 0 -1 0 1)
	(make-line-stencil lrw 0 1 1 1)
        ) 
       lrb 0 0
       )
      (cons lrx lry)
     )

     (ly:stencil-translate
      (ly:stencil-rotate-absolute
       (ly:stencil-add 
	(make-line-stencil flw 0 -1 0 0.75)
	(make-line-stencil flw 0 0.75 -0.25 1)
	(make-line-stencil flw -0.25 1 -0.75 1)
	(make-line-stencil flw -0.75 1 -1 0.75)
        ) 
       flb 0 0
       )
      (cons flx fly)
     )

     (ly:stencil-translate
      (ly:stencil-rotate-absolute
       (ly:stencil-add 
	(make-line-stencil frw 0 -1 0 0.75)
	(make-line-stencil frw 0 0.75 0.25 1)
	(make-line-stencil frw 0.25 1 0.75 1)
	(make-line-stencil frw 0.75 1 1 0.75)
        ) 
       frb 0 0
       )
      (cons frx fry)
     )

     (ly:stencil-translate
      (ly:stencil-rotate-absolute
       (ly:stencil-add 
	(make-line-stencil flw 0 -1 0 0.75)
	(make-line-stencil flw 0 0.75 -0.25 1)
	(make-line-stencil flw -0.25 1 -0.75 1)
	(make-line-stencil flw -0.75 1 -1 0.75)
        ) 
       flb 0 0
       )
      (cons flx fly)
     )

     (ly:stencil-translate
      (ly:stencil-rotate-absolute
       (ly:stencil-add 
	(make-line-stencil frw 0 -1 0 0.75)
	(make-line-stencil frw 0 0.75 0.25 1)
	(make-line-stencil frw 0.25 1 0.75 1)
	(make-line-stencil frw 0.75 1 1 0.75)
        ) 
       frb 0 0
       )
      (cons frx fry)
     )

     (ly:stencil-add 
      (make-line-stencil boxth boxllx boxlly boxurx boxlly)
      (make-line-stencil boxth boxurx boxlly boxurx boxury)
      (make-line-stencil boxth boxurx boxury boxllx boxury)
      (make-line-stencil boxth boxllx boxury boxllx boxlly)
     )

     (cond 
      
      ((string=? dur-string "1  ") 
       (begin
        (ly:stencil-add 
         (make-line-stencil boxth boxllx (- boxlly 1) boxurx (- boxlly 1))
        )
       )
      )
      
      ((string=? dur-string "2  ") 
       (begin
        (ly:stencil-add 
         (make-line-stencil boxth boxllx (- boxlly 1) boxurm (- boxlly 1))
        )
       )
      )
      
      ((string=? dur-string "4  ") 
       (begin
        (ly:stencil-add 
         (make-line-stencil boxth boxllx (- boxlly 1) boxurv (- boxlly 1))
        )
       )
      )
      
      ((string=? dur-string "8  ") 
       (begin
        (ly:stencil-add 
         (make-line-stencil boxth boxllx boxlly boxllx (- boxlly 2))
        )
       )
      )
      
      
     )

   )
 ) 
)






\version "2.18.2"

\header {
  title = "base con cruce"
}

soprano = \relative c'' {
  \time 4/4
  \key c \major
  \tempo 4=50
  r1
  r1
  a4. b8 c4 a | \break
  g4. a8 b4 g |
  f4. g8 a4 f4 | \break
  e2  gis2 |
  a4. b8 c4 a | \break
  g4. a8 b4 g |
  f4. g8 a4 f4 | \break
  e2  a2 |

}

tango = \relative c'' {
 \clef percussion
 s1
 s1_\markup \tango-pose #'"ll 5304 lr 6309 fl 6749 fr 5744 dur 1  " 
 s2_\markup \tango-pose #'"ll 4309 lr 8304 fl 8744 fr 4749 dur 2  " 
 s2_\markup \tango-pose #'"ll 6104 lr 7509 fl 7949 fr 6544 dur 2  " 
 s2_\markup \tango-pose #'"ll 6509 lr 7104 fl 7544 fr 6949 dur 2  " 
 s2_\markup \tango-pose #'"ll 6304 lr 7309 fl 3749 fr 6844 dur 2  " 
 s2_\markup \tango-pose #'"ll 6409 lr 7104 fl 3544 fr 5949 dur 2  " 
 s2_\markup \tango-pose #'"ll 4204 lr 8309 fl 8749 fr 4744 dur 2  " 
 s2_\markup \tango-pose #'"ll 5308 lr 6304 fl 6744 fr 5749 dur 2  " 
 s2_\markup \tango-pose #'"ll 5304 lr 6309 fl 6749 fr 5744 dur 2  " 
 s2_\markup \tango-pose #'"ll 4309 lr 8304 fl 8744 fr 4749 dur 2  " 
 s2_\markup \tango-pose #'"ll 6104 lr 7509 fl 7949 fr 6544 dur 2  " 
 s2_\markup \tango-pose #'"ll 6509 lr 7104 fl 7544 fr 6949 dur 2  " 
 s2_\markup \tango-pose #'"ll 6304 lr 7309 fl 3749 fr 6844 dur 2  " 
 s2_\markup \tango-pose #'"ll 6409 lr 7104 fl 3544 fr 5949 dur 2  " 
 s2_\markup \tango-pose #'"ll 4204 lr 8309 fl 8749 fr 4744 dur 2  " 
 s1_\markup \tango-pose #'"ll 5304 lr 6309 fl 6749 fr 5744 dur 1  " 
 }

\score {
  \new StaffGroup
  <<
    \new Staff {
    \new Voice { \soprano }
    }
    \new Staff { 
      \override Staff.StaffSymbol.line-count = #1
      \override Staff.StaffSymbol.line-positions = #'(6)
      \new Voice { \tango } 
    }
  >>
  \layout {
    \context {
      \Score
      \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/128)
    }
  }
}
