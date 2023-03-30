

```mermaid 

  classDiagram
      Pelaaja --> Nopat
      Nopat "+1...12" --> Pelaaja
      Pelaaja "min 2. max 8." --> Pelilauta

    class Pelilauta{
        Ruutu1
        ...
        Ruutu40

    }

    class Nopat{
        noppa1
        noppa2
    }


      class Pelaaja{
          pelinappula
          ruutu
      }    

```
