(deffacts Suspects
  (Sus  A 0)
  (Sus  B 1)
  (Sus  C 2)
)


(defrule Suspects1
(Sus ?name ?partners)
(test (= ?partners 0)) 
=>
(assert (sus isnt ?name ) 
))


(defrule Suspects2
(Sus ?name ?partners)
(test (= ?partners 1)) 
=>
(bind ?n sus is C)
(bind ?k sus is D )
(assert  (sus is C )(sus is D )
))


(defrule Suspends_check
(Sus ?name ?partners )
(forall(Sus ?name ?partners)
(sus is C ))
=>
(assert (sus is B or C , D ) 
(printout t "B or C , D to jail " crlf ))
)



(defrule Suspects5
(forall(Sus ?name ?partners)
(sus is D )
(sus is B or C , D ) )
=>
(printout t  "D go to jail" crlf ))