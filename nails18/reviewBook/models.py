from django.db import models


class Review(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    text = models.TextField(
        verbose_name="Текст отзыва"
    )
    is_checked = models.BooleanField(
        default=False,
        verbose_name="Проверено"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.full_name} ({'проверен' if self.is_checked else 'не проверен'})"

    class Meta:
        ordering = ['-created_at']
