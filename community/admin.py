from django.contrib import admin

from .models import NFT, Wallet, DiscordRole, DiscordUser, DiscordUserRole, Person


@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('eth_address', 'wallet_type', 'alise',)


@admin.register(DiscordRole)
class DiscordRoleAdmin(admin.ModelAdmin):
    list_display = ('alise', 'discord_id',)


@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'alise', 'discord_id',)


@admin.register(DiscordUserRole)
class DiscordUserRoleAdmin(admin.ModelAdmin):
    list_display = ('discord_user', 'discord_role',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
