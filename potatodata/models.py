from django.db import models

class LinkCategory(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class LinkSubcategory(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class PotatoLink(models.Model):
    text = models.CharField(max_length = 50)
    category = models.ForeignKey(LinkCategory)
    subcategory = models.ForeignKey(LinkSubcategory, null=True, blank=True)
    url = models.URLField(max_length = 200)
    description = models.CharField(max_length = 200, blank=True)

    def __str__(self):
        return self.text

class napmnRegion(models.Model):
    napmn_name = models.CharField(max_length = 32)
    
    def __str__(self):
        return self.napmn_name
        
# Start of SPP Tables
class Variety(models.Model):
    usda_name = models.CharField(unique=True, max_length=30)
    napmn_name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.usda_name


class Subvariety(models.Model):
    usda_name = models.CharField(unique=True, max_length=30)
    napmn_name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.usda_name

class Grade(models.Model):
    usda_name = models.CharField(unique=True, max_length=30)
    napmn_name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.usda_name


class Package(models.Model):
    usda_name = models.CharField(unique=True, max_length=50)
    napmn_name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.usda_name


class Size(models.Model):
    usda_name = models.CharField(unique=True, max_length=50)
    napmn_name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.usda_name


class ShippingDistrict(models.Model):
    usda_name = models.CharField(unique=True, max_length=100)
    napmn_name = models.ForeignKey(napmnRegion, null=True)
    
    def __str__(self):
        return self.usda_name


class ShippingPointPrice(models.Model):
    report_date = models.DateField()
    shipping_district = models.ForeignKey(ShippingDistrict)
    season = models.PositiveSmallIntegerField()  # This field type is a guess.
    variety = models.ForeignKey(Variety)
    subvariety = models.ForeignKey(Subvariety)
    grade = models.ForeignKey(Grade)
    package = models.ForeignKey(Package)
    size = models.ForeignKey(Size)
    low = models.DecimalField(max_digits=6, decimal_places=2)
    high = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    mostly_low = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    mostly_high = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    price_weight = models.IntegerField()

    def get_cwt_price(self):
        temp = [self.low, self.high, self.mostly_low, self.mostly_high]
        prices = []
        for price in temp:
            if price:
                prices.append(price)
            else:
                break
        if len(prices) > 2:
            prices = prices[2:]

        return (float(prices[0]) + float(prices[-1])) * (50/self.price_weight)

    class Meta:
        unique_together = (('report_date', 'shipping_district', 'variety', 'subvariety', 'grade', 'package', 'size'),)
# End SPP Tables

# Start of Truckrate Tables
class FreightDestination(models.Model):
    usda_name = models.CharField(unique=True, max_length=50)


class TruckRate(models.Model):
    week_ending = models.DateField()
    shipping_district = models.ForeignKey(ShippingDistrict)
    freight_destination = models.ForeignKey(FreightDestination)
    week_low = models.IntegerField()
    week_high = models.IntegerField(blank=False, null=True)
    day_low = models.IntegerField(blank=False, null=True)
    day_high = models.IntegerField(blank=False, null=True)
    price_weight = models.IntegerField()
    
    class Meta:
        unique_together = (('week_ending', 'shipping_district', 'freight_destination'),)
# End Truckrate Tables

# Start of Movement Tables
class Origin(models.Model):
    usda_name = models.CharField(unique=True, max_length=60)

class MovementDistrict(models.Model):
    usda_name = models.CharField(unique=True, max_length=60)

class Movement(models.Model):
    week_ending = models.DateField()
    origin = models.ForeignKey(Origin)
    movement_district = models.ForeignKey(MovementDistrict)
    season = models.PositiveSmallIntegerField()
    variety = models.ForeignKey(Variety)
    organic = models.IntegerField()
    import_export = models.CharField(max_length=8)
    transport_mode = models.CharField(max_length=9)
    total_weight = models.IntegerField()
    
    class Meta:
        unique_together = (('week_ending', 'origin', 'movement_district', 'season', 'variety', 'organic', 'import_export', 'transport_mode'),)
# End Movement Tables

class FWA(models.Model):
    date = models.DateField()
    napmn_region = models.ForeignKey(napmnRegion)
    subvariety = models.ForeignKey(Subvariety)
    fwa = models.DecimalField(max_digits=6, decimal_places=3)
    
    class Meta:
        unique_together = (('date', 'napmn_region', 'subvariety'),)

class GRI(models.Model):
    date = models.DateField()
    napmn_region = models.ForeignKey(napmnRegion)
    subvariety = models.ForeignKey(Subvariety)
    gri = models.DecimalField(max_digits=6, decimal_places=3)
    
    class Meta:
        unique_together = (('date', 'napmn_region', 'subvariety'),)
