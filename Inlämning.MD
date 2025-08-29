# DI-CONTIANER 
Jag skrev ett gränsnsit för BookingService genom att skapa IBookingService.cs, För att förbättra underhållbarheten och testbarheten av koden. Det gör en tydlig separation mellan kontrollern och services, vilket följer principen för Dependency Injection (DI).  Istället för att instansiera BookingService direkt inom BookingController modifierade jag konstruktorn för att ta emot en IBookingService-parameter, vilket gör att DI-containern kan injicera den lämpliga tjänsteinstansen när kontrollern skapas. Genom att atddera scope i program.cs:
```
builder.Services.AddScoped<IBookingService, BookingService>();
```
Denna metod främjar lös koppling, eftersom kontrollern är mindre beroende av den specifika implementeringen av tjänsten, vilket gör det enklare att byta ut implementationer eller mocka tjänsten för tester. 

# DRY-princip
För att följa DRY-principen (Don't Repeat Yourself), Har jag ändrat controller genom att try-catch:
```
try
{
}
catch (InvalidOperationException ex)
{
    return Conflict(ex.Message);
}
```
Så behöver man inte kontrollera/kalla igen methoden ```HasOverlap(...)```, istället ska man använder try-catch. Med all överlappningslogik på en plats kan framtida modifieringar göras mer effektivt, och risken för att introducera buggar på grund av duplicerad kod minimeras, vilket resulterar i en tydligare kodstruktur.
