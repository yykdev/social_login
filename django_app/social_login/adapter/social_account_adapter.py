import json

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        print(sociallogin.account.get_avatar_url())
        return super(SocialAccountAdapter, self).pre_social_login(
            request,
            sociallogin
        )

    def save_user(self, request, sociallogin, form=None):

        return super(SocialAccountAdapter, self).save_user(
            request,
            sociallogin,
            form
        )