#Viikko3 tehtävä 2: Laajennettu monopoli 

```mermaid 

  classDiagram
      Pelaaja --> Nopat
      Nopat "+2..12" --> Pelaaja : pelaaja.ruutu + "2..12"
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

