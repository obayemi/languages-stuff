#!/usr/bin/sbcl --script
;; author: obayemi

(defun calc_phi (phi iters)
  "Compute golden number phi"
  ;; uncoment next line to add per recurtion logging
  ;;(format t "~D: ~F~%" iters phi)
  (if (> iters 0)
   (calc_phi (+ (/ 1 phi) 1) (1- iters))
   phi))

(defun main(&key (base 2) (iters 10))
  (format t "Phi from ~F after ~D recursions: ~F~%"
          base iters (calc_phi base iters)))

(let* ((tmpiters (nth 1 sb-ext:*posix-argv*))
      (tmpbase (nth 2 sb-ext:*posix-argv*))
      (iters (if tmpiters (parse-integer tmpiters) 10))
      (base (if tmpbase (parse-integer tmpbase) 2.0)))
  (main :iters iters :base base))
;; (print sb-ext:*posix-argv*)
