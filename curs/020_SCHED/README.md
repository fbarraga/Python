# Schedule 

htogramación de trabajos de Python para humanos. Ejecute funciones de Python (o cualquier otra invocable) periódicamente utilizando una sintaxis descriptiva.

Una API fácil de usar para programar trabajos, hecha para humanos.
Programador en proceso para trabajos periódicos. ¡No se necesitan procesos adicionales!
Muy ligero y sin dependencias externas.
Excelente cobertura de prueba.
Probado en Python 3.7, 3.8, 3.9, 3.10 y 3.11

## Ejemplos

### Ejemplo básico

```python
$ pip install schedule
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

Más ejemplos

### Ejecutar un trabajo cada x minutos

```python
import schedule
import time

def job():
    print("I'm working...")

# Run job every 3 second/minute/hour/day/week,
# Starting 3 second/minute/hour/day/week from now
schedule.every(3).seconds.do(job)
schedule.every(3).minutes.do(job)
schedule.every(3).hours.do(job)
schedule.every(3).days.do(job)
schedule.every(3).weeks.do(job)

# Run job every minute at the 23rd second
schedule.every().minute.at(":23").do(job)

# Run job every hour at the 42nd minute
schedule.every().hour.at(":42").do(job)

# Run jobs every 5th hour, 20 minutes and 30 seconds in.
# If current time is 02:00, first execution is at 06:20:30
schedule.every(5).hours.at("20:30").do(job)

# Run job every day at specific HH:MM and next HH:MM:SS
schedule.every().day.at("10:30").do(job)
schedule.every().day.at("10:30:42").do(job)
schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)

# Run job on a specific day of the week
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

### Usar un decorador para programar un trabajo

Utilice el para programar una función. Páselo un intervalo usando la misma sintaxis que la anterior mientras omite el .@repeat.do()

```python
from schedule import every, repeat, run_pending
import time

@repeat(every(10).minutes)
def job():
    print("I am a scheduled job")

while True:
    run_pending()
    time.sleep(1)
El decorador no trabaja en métodos de clase no estáticos.@repeat

```

### Pasar argumentos a un trabajo

do() Pasa argumentos adicionales a la función de trabajo

```python
import schedule

def greet(name):
    print('Hello', name)

schedule.every(2).seconds.do(greet, name='Alice')
schedule.every(4).seconds.do(greet, name='Bob')

from schedule import every, repeat

@repeat(every().second, "World")
@repeat(every().day, "Mars")
def hello(planet):
    print("Hello", planet)
```

### Cancelar un trabajo

Para quitar un trabajo del programador, utilice el métodoschedule.cancel_job(job)

```python
import schedule

def some_task():
    print('Hello world')

job = schedule.every().day.at('22:30').do(some_task)
schedule.cancel_job(job)
```

### Ejecutar un trabajo una vez

Volver de un trabajo para quitarlo del programador.schedule.CancelJob

```python
import schedule
import time

def job_that_executes_once():
    # Do some work that only needs to happen once...
    return schedule.CancelJob

schedule.every().day.at('22:30').do(job_that_executes_once)

while True:
    schedule.run_pending()
    time.sleep(1)
```

### Consigue todos los trabajos

Para recuperar todos los trabajos del programador, utilice schedule.get_jobs()

```python
import schedule

def hello():
    print('Hello world')

schedule.every().second.do(hello)

all_jobs = schedule.get_jobs()
```

### Cancelar todos los trabajos

Para quitar todos los trabajos del programador, utilice schedule.clear()

```python
import schedule

def greet(name):
    print('Hello {}'.format(name))

schedule.every().second.do(greet)

schedule.clear()
```

### Obtener varios trabajos, filtrados por etiquetas

Puede recuperar un grupo de trabajos del programador, seleccionándolos mediante un identificador único.

```python
import schedule

def greet(name):
    print('Hello {}'.format(name))

schedule.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
schedule.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
schedule.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')

friends = schedule.get_jobs('friend')
Devolverá una lista de todos los trabajos etiquetados como .friend
```

### Cancelar varios trabajos, filtrados por etiquetas

Puede cancelar la programación de un grupo de trabajos seleccionándolos mediante un identificador único.

```python
import schedule

def greet(name):
    print('Hello {}'.format(name))

schedule.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
schedule.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
schedule.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')

schedule.clear('daily-tasks')
Evitará que todos los trabajos etiquetados como se vuelvan a ejecutar.daily-tasks
```

### Ejecutar un trabajo a intervalos aleatorios

```python

def my_job():
    print('Foo')

# Run every 5 to 10 seconds.
schedule.every(5).to(10).seconds.do(my_job)
every(A).to(B).seconds ejecuta la función de trabajo cada N segundos de tal manera que A <= N <= B.

Ejecutar un trabajo hasta un momento determinado
import schedule
from datetime import datetime, timedelta, time

def job():
    print('Boo')

# run job until a 18:30 today
schedule.every(1).hours.until("18:30").do(job)

# run job until a 2030-01-01 18:33 today
schedule.every(1).hours.until("2030-01-01 18:33").do(job)

# Schedule a job to run for the next 8 hours
schedule.every(1).hours.until(timedelta(hours=8)).do(job)

# Run my_job until today 11:33:42
schedule.every(1).hours.until(time(11, 33, 42)).do(job)

# run job until a specific datetime
schedule.every(1).hours.until(datetime(2020, 5, 17, 11, 36, 20)).do(job)
```
El método establece la fecha límite de trabajos. El trabajo no se ejecutará después de la fecha límite.until

### Tiempo hasta la próxima ejecución

Se usa para obtener el número de segundos hasta que se programe la ejecución del siguiente trabajo. El valor devuelto es negativo si los siguientes trabajos programados se programaron para ejecutarse en el pasado. Devuelve si no hay trabajos programados.schedule.idle_seconds()None

```python
import schedule
import time

def job():
    print('Hello')

schedule.every(5).seconds.do(job)

while 1:
    n = schedule.idle_seconds()
    if n is None:
        # no more jobs
        break
    elif n > 0:
        # sleep exactly the right amount of time
        time.sleep(n)
    schedule.run_pending()
```

### Ejecute todos los trabajos ahora, independientemente de su programación

Para ejecutar todos los trabajos, independientemente de si están programados para ejecutarse o no, utilice . Los trabajos se reprograman después de finalizar, tal como lo harían si se ejecutaran con .schedule.run_all()run_pending()

```python
import schedule

def job_1():
    print('Foo')

def job_2():
    print('Bar')

schedule.every().monday.at("12:40").do(job_1)
schedule.every().tuesday.at("16:40").do(job_2)

schedule.run_all()

# Add the delay_seconds argument to run the jobs with a number
# of seconds delay in between.
schedule.run_all(delay_seconds=10)
```

## Cuándo no usar Schedule

Seamos honestos, Schedule no es una biblioteca de programación de "talla única". Esta biblioteca está diseñada para ser una solución simple para problemas de programación simples. Probablemente deberías buscar en otro lugar si necesitas:

Persistencia en el trabajo (recuerde el horario entre reinicios)
Temporización exacta (ejecución de precisión inferior a un segundo)
Ejecución simultánea (varios subprocesos)
Localización (días laborables o festivos)
La programación no tiene en cuenta el tiempo que tarda la función de trabajo en ejecutarse. Para garantizar una programación de ejecución estable, debe mover los trabajos de ejecución prolongada fuera del subproceso principal (donde se ejecuta el programador). Consulte Ejecución paralela para obtener una implementación de ejemplo.