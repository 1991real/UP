from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип мандарина"
        verbose_name_plural = "Типы мандаринов"


class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name="Цвет")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class CountryProduction(models.Model):
    country = models.CharField(max_length=30, verbose_name="Страна")

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Страна производитель"
        verbose_name_plural = "Страны производители"


class Mandarin(models.Model):
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Тип"
    )

    country = models.ForeignKey(
        CountryProduction,
        on_delete=models.CASCADE,
        verbose_name="Страна"
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name="Цвет"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    image = models.ImageField(
        upload_to="mandarins/",
        verbose_name="Изображение"
    )

    def __str__(self):
        return f"{self.type} ({self.country})"

    class Meta:
        verbose_name = "Мандарин"
        verbose_name_plural = "Мандарины"


class Review(models.Model):
    mandarin = models.ForeignKey(
        Mandarin,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Мандарин"
    )

    rating = models.SmallIntegerField(verbose_name="Оценка")
    comment = models.CharField(max_length=500, verbose_name="Комментарий")

    def __str__(self):
        return f"Отзыв #{self.id}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"