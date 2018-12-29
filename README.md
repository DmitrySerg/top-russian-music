# Тематическое моделирование слушателей

Идея - хотим узнать, чем отличаются пользователи vk, слушающие разные жанры музыки

Для этого хотим найти по топ-10 исполнителей по разным жанрам и выкачать их комментарии, подписчиков, а также стены и топ-5 подписок. Далее можем запилить тематическое моделирование по комментам/стенам, а также оценку тональности по комментам. В результате хотим получить тематические портреты средних слушателей разных жанров и сравнить их. 

Текущий план:
- Найти 2 самых противоположных жанра
- Найти топ-10 исполнителей (по сути - топ-10 самых больших групп вк) по этим жанрам
- Выкачать датку
- Посмотреть, получаются ли разумные модели

Классика:
1. https://vk.com/classic_relax (95к)
2. https://vk.com/classicalmusic.classic (53к, но комменты отключены)
3. https://vk.com/classic_best (30к)
4. https://vk.com/classic_online (24k, тоже отключены комменты)
5. https://vk.com/inclassic (22к)
6. https://vk.com/classicstories (22к)
7. https://vk.com/classical_music_guide (8k)
8. https://vk.com/contemporary_classical (14k, очень мало комментов)
9. https://vk.com/pi_a_no (19k)
10. https://vk.com/petertchaikovsky (22k)
11. https://vk.com/wmozart (93k)
12. https://vk.com/ludvigvonbeethoven (35k

```python
classic: {
	"https://vk.com/classic_relax",
	"https://vk.com/classicalmusic.classic",
	"https://vk.com/classic_best",
	"https://vk.com/classic_online",
	"https://vk.com/inclassic",
	"https://vk.com/classicstories",
	"https://vk.com/classical_music_guide",
	"https://vk.com/contemporary_classical",
	"https://vk.com/pi_a_no",
	"https://vk.com/petertchaikovsky",
	"https://vk.com/wmozart",
	"https://vk.com/ludvigvonbeethoven"
}
```