from django.db import models
from django.db.models.deletion import PROTECT


class Person(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class NFT(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    nft_id = models.CharField(max_length=255)
    opensea_url = models.CharField(max_length=512)
    original_count = models.IntegerField()
    private_notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    def __str__(self):
        return self.name


class Wallet(models.Model):
    person = models.ForeignKey(Person, on_delete=PROTECT, blank=True, null=True)
    eth_address = models.CharField(max_length=255)
    wallet_type = models.CharField(max_length=255)
    alise = models.CharField(max_length=255)

    def __str__(self):
        return self.person


class DiscordRole(models.Model):
    alise = models.CharField(max_length=255)
    discord_id = models.CharField(max_length=255)


class DiscordUser(models.Model):
    person = models.ForeignKey(Person, on_delete=PROTECT, blank=True, null=True)
    display_name = models.CharField(max_length=255)
    alise = models.CharField(max_length=255, blank=True, null=True)
    discord_id = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.display_name


class DiscordUserRole(models.Model):
    discord_user = models.ForeignKey(DiscordUser, on_delete=PROTECT)
    discord_role = models.ForeignKey(DiscordRole, on_delete=PROTECT)
    notes = models.TextField(blank=True, null=True)
