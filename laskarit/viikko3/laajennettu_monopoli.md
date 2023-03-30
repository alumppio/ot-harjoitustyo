#Viikko3 tehtävä 2: Laajennettu monopoli 

```mermaid 

  classDiagram
      Pelaaja --> Nopat
      Nopat "+2...12" --> Pelaaja : pelaaja.ruutu + noppa1 + noppa2
      Pelaaja "min 2. max 8." --> Pelilauta

    class Pelilauta{
        Katu1
        ...
        Katu4

    }

    class Aloitusruutu{
        pelaajat
        sijainti
    }
    
    class Mannerheimintie{
        Ruutu1
        ...
        Ruutu10
    }


    class Erottaja{
        Ruutu11
        ...
        Ruutu20
    }

    class Mannerheimintie{
        Ruutu20
        ...
        Ruutu10
    }

    class Nopat{
        noppa1
        noppa2
    }


      class Pelaaja{
          pelinappula
          ruutu
          raha
      }    


    class Vankila{
        pelaajat
        sijainti
    }

    class Sattuma ja yhteismaa{
        kortti
        sijainti
    }

    class Asemat ja laitokset{
        omistaja
        sijainti
    }



```

