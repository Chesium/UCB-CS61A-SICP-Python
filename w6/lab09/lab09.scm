(define (over-or-under num1 num2) (
  if (< num1 num2) 
    -1 
    (if (= num1 num2)
      0
      1
)))

(define (make-adder num) (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n) (if (= n 1)
  f
  (composed (repeat f (- n 1)) f))
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) (begin 
  (define mi (min a b))
  (define mx (max a b))
  (if (= (modulo mx mi) 0)
    mi
    (gcd mi (modulo mx mi))
  )
))

(define (duplicate lst) 
  (if (null? lst)
    `()
    (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
  )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
  (if (null? s)
    `()
    (if (list? (car s))
      (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
      (cons (fn (car s)) (deep-map fn (cdr s)))
    )
  )
)
