(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (list keys values))

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist)
  (cadr kwlist))

(define (make-kwlist2 keys values)
  (if (null? keys)
    nil
    (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
  ))

(define (get-keys-kwlist2 kwlist)
  (if (null? kwlist)
    nil
    (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist)))
  ))

(define (get-values-kwlist2 kwlist)
  (if (null? kwlist)
    nil
    (cons (cadr (car kwlist)) (get-values-kwlist2 (cdr kwlist)))
  ))


(define (add-to-kwlist kwlist key value)
  (make-kwlist (append (get-keys-kwlist kwlist) (list key)) (append (get-values-kwlist kwlist) (list value))))

(define (get-first-from-kwlist kwlist key)
    (let ((k (get-keys-kwlist kwlist)) (v (get-values-kwlist kwlist)))
      (if (null? k)
        nil
        (if (eq? (car k) key)
          (car v)
          ; (car v)
          ; (get-first-from-kwlist (make-kwlist '(a b c) '(1 2 3)) 'a)
          (get-first-from-kwlist (make-kwlist (cdr k) (cdr v)) key)
        )
      )
    )
)

