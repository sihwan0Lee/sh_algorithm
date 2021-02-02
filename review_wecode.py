import json
from django.views import View
from django.http import JsonResponse
from .models import ItemReview
from aboutteatime.utils import login decorator

class ReviewWrite(View):
    @logindecorator
    def post(self, request, item_id):
        try:
            if Item.objects.filter(id=item_id).exist():
                # 모델클래스 아이템에서 아이디변수 = 아이템_id인게 존재한다면
                data = json.loads(request.body)
                # 데이터는 리퀘스트의 바디에 제이슨 형태로 받을 것이다.
                Review(
                    user             = request.user,
                    image_url        = data['image_url'],
                    content          = data['content'],
                    packaging_rating = data['packaging_rating'],
                    fragrance_rating = data['fragrance_rating'],
                    taste_rating     = data['taste_rating'],
                    itemreviewlike   = data['itemreviewlike'],
                    overall_rating   = data['overall_rating'],
                 ).save()
            return JsonResponse({'comments':list(ItemReview.objects.values())}, status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID KEY'}, status=400)
# 이부분 select_related , prefetch_related 공부할것

class ReviewRead(View):
    def get(self, request, item_id):
        cur_item = Item.objects.get(id=item_id)
        cache = cur_item.prefetch_related('itemreview_set')
        reviews = []

        for review in cache.review_set:
            image_list = []
            images = review.images.all()
            for image in images:
                image_list.append(image.image_url)
            review_dict = {
                'user' = review.user.username,
                'created_at' = review.created_at,
                'img_url' = image_list,
                'content' = review.content,
                'packaging_rating' = reivew.packaging_rating,
                'fragrance_rating' = review.fragrance_rating,
                'taste_rating' = review.taste_rating,
                'overall_rating' = review.overall_rating
            }
            review_dict['item_title'] = cur_item.title
            reviews.append(review_dict)
        
        return JsonResponse({'reviews':reviews}, status=200)
