# # --> create or update white diamonds
# def white_diamonds(request):

#     def update_max_min(queryset):
#         # <-- get max / min values from diamonds
#         values = [
#             {   
#                 'name': 'carat',
#                 'min': queryset.order_by('weight')[0].weight,
#                 'max': queryset.order_by('-weight')[0].weight,
#             },
#             {   
#                 'name': 'depth',
#                 'min': queryset.order_by('depth')[0].depth,
#                 'max': queryset.order_by('-depth')[0].depth,
#             },
#             {   
#                 'name': 'depth_procent',
#                 'min': queryset.order_by('depth_procent')[0].depth_procent,
#                 'max': queryset.order_by('-depth_procent')[0].depth_procent,
#             },
#             {   
#                 'name': 'length',
#                 'min': queryset.order_by('length')[0].length,
#                 'max': queryset.order_by('-length')[0].length,
#             },
#             {   
#                 'name': 'ratio',
#                 'min': queryset.order_by('lw')[0].lw,
#                 'max': queryset.order_by('-lw')[0].lw,
#             },
#             {   
#                 'name': 'sale_price',
#                 'min': queryset.order_by('sale_price')[0].sale_price,
#                 'max': queryset.order_by('-sale_price')[0].sale_price,
#             },
#             {   
#                 'name': 'table',
#                 'min': queryset.order_by('table_procent')[0].table_procent,
#                 'max': queryset.order_by('-table_procent')[0].table_procent,
#             },
#             {   
#                 'name': 'width',
#                 'min': queryset.order_by('width')[0].width,
#                 'max': queryset.order_by('-width')[0].width,
#             },
#         ]
        
#         # <-- get max / min filter objects 
#         max_min = MaxMin.objects.all()
        
#         # --> update max / min values
#         for value in values:
#             for item in max_min:
#                 if item.name == value['name']:
#                     item.min = value['min']
#                     item.max = value['max']
#                     item.save()

#     # @ not auth
#     if not request.user.is_authenticated:
#         return redirect(reverse_lazy('user_info'))

#     # ? this url
#     this_url = 'white_diamonds'

#     # ? get form
#     form = UploadDiamondForm()

#     # ? msg var
#     msg = False

#     # @ POST
#     if request.method == 'POST':

#         # * get file
#         file = request.FILES['diamonds']
        
#         # * check file type
#         if not file.name.endswith('.csv'):
#             messages.error(request, 'The uploaded file must be in the format: CSV')
#             return redirect(reverse_lazy(this_url))

#         # * get form
#         form = UploadDiamondForm(request.POST)
        
#         # * decode and read file
#         file = request.FILES['diamonds'] 
#         decoded_file = file.read().decode('utf-8').splitlines()
#         reader = csv.DictReader(decoded_file, delimiter=";")

#         # * read file + create diamond items
#         diamonds = []
#         for row in reader:
#             # * get or create shape item
#             try:
#                 shape = row['Shape'],
#             except KeyError:
#                 messages.error(request, 'The submitted file is not a file with new stones')
#                 return redirect(reverse_lazy(this_url))
                
#             # * get disc
#             disc = round(float(row['Sale Price'].replace(',', '.')) / float(row['Weight'].replace(',', '.')) / float(row['Rap. price'].replace(',', '.')) , 1)
#             disc = round(disc * 2, 2)

#             # * get clarity num
#             clarity_list = ['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FI']
#             for index, value in enumerate(clarity_list):
#                 if value == row['Clarity']:
#                     clarity_value = index

#             # * get cut num
#             cut_list = ['N/A','Fair','Good','Very Good','Ideal','Super Ideal','Excellent']
#             for index, value in enumerate(cut_list):
#                 if value == row['Cut']:
#                     cut_value = index

#             # * get color num
#             color_list = ['M','L','K','J','I','H','G','F','E','D']
#             for index, value in enumerate(color_list):
#                 if value == row['Color']:
#                     color_value = index

#             # * get polish num
#             polish_list = ['Good','Very Good','Excellent', 'N/A']
#             for index, value in enumerate(polish_list):
#                 if value == row['Polish']:
#                     polish_value = index

#             # * get symmetry num
#             symmetry_list = ['N/A','Good','Very Good','Excellent']
#             for index, value in enumerate(symmetry_list):
#                 if value == row['Symmetry']:
#                     symmetry_value = index

#             # * get fluour num
#             fluour_list = ['None','Faint','Medium','Strong','Very Strong']
#             for index, value in enumerate(fluour_list):
#                 if value == row['Fluor. Note']:
#                     fluour_value = index

#             # * get shape num
#             shape_list = ['Round', 'Marquise', 'Asscher', 'Cushion', 'Emerald', 'Heart', 'Oval', 'Pear', 'Princess', 'Radiant']
#             shape_value = 10
#             for index, value in enumerate(shape_list):
#                 if value == row['Shape']:
#                     shape_value = index
                
#             # * get lab num
#             lab_list = ['IGI', 'GIA', 'GCAL', 'HDR']
#             lab_value = 0
#             for index, value in enumerate(lab_list):
#                 if value == row['Cert. Company']:
#                     lab_value = index

#             # --> create diamond
#             diamond = {
#                 'ref': row['Ref'],
#                 'vendor': row['Vendor'],
#                 'vendor_id': row['Vendor ID'],
#                 'cert_number': row['Cert. Number'],

#                 'shape': shape_value,
#                 'shape_ex': row['Shape Ex'],
                
#                 'weight': row['Weight'].replace(',', '.'),
#                 'color': color_value,
#                 'color_comment': row['Color Comment'],
#                 'clarity': clarity_value,

#                 'rap_1ct': row['Rap. 1ct'].replace(',', '.'),
#                 'rap_price': row['Rap. price'].replace(',', '.'),
#                 'sale_price': round(float(row['Sale Price'].replace(',', '.')), 0),
#                 'disc': disc,

#                 'origin': row['Origin'],
#                 'cut': cut_value,
#                 'polish': polish_value,
#                 'symmetry': symmetry_value,

#                 'gridle_from': row['Girdle From'],
#                 'gridle_to': row['Girdle To'],
#                 'gridle_type': row['Girdle Type'],
#                 'culet': row['Culet'],
#                 'fluorescence': row['Fluorescence'],
#                 'fluor': fluour_value,

#                 'length': row['Length'].replace(',', '.'),
#                 'width': row['Width'].replace(',', '.'),
#                 'depth': row['Depth'].replace(',', '.'),
#                 'lw': round(float(row['Length'].replace(',', '.')) / float(row['Width'].replace(',', '.')), 2),

#                 'cert_company': lab_value,
#                 'depth_procent': row['Depth %'].replace(',', '.'),
#                 'table_procent': row['Table %'].replace(',', '.'),
#                 'warehouse': row['Warehouse'],
#                 'comments': row['Comments'],
#                 'photo': row['Photo'],
#                 'video': row['Video'],
                
#                 'on_memo': row['On Memo'],
#                 'report_link': row['Report Link'],

#                 'key': f"{row['Ref']};{row['Vendor']};{row['Cert. Number']};{row['Color']};{row['Clarity']}",

#             }

#             # -->  create diamonds array
#             diamonds.append(diamond)

#         # * create action enumerate vaelu
#         num_created = 0
#         num_updated = 0

#         # --> update or crete diamond in model
#         for diamond in diamonds:
            
#             # * create this key and this shape var
#             key = diamond['key']

#             stone, created = Diamond_Model.objects.update_or_create(key=key, defaults=diamond)

#             if created:
#                 num_created += 1
#             else:
#                 num_updated += 1

#         # * get max / min values
#         queryset = Diamond_Model.objects.all()
#         update_max_min(queryset)


#         # * success message
#         msg = f"Created Stones: {num_created} | Updated Stones: {num_updated}"
#         messages.success(request, 'The data was uploaded successfully')

#     # * create context   
#     context = {
#         'title': 'Upload a whitelist',
#         'form': form,
#         'msg': msg
#     }

#     return render(request, 'upload_diamonds.html', context)



def white_diamonds(request):
    def update_max_min(queryset):
        # <-- get max / min values from diamonds
        values = [
            {   
                'name': 'carat',
                'min': queryset.order_by('weight')[0].weight,
                'max': queryset.order_by('-weight')[0].weight,
            },
            {   
                'name': 'depth',
                'min': queryset.order_by('depth')[0].depth,
                'max': queryset.order_by('-depth')[0].depth,
            },
            {   
                'name': 'depth_procent',
                'min': queryset.order_by('depth_procent')[0].depth_procent,
                'max': queryset.order_by('-depth_procent')[0].depth_procent,
            },
            {   
                'name': 'length',
                'min': queryset.order_by('length')[0].length,
                'max': queryset.order_by('-length')[0].length,
            },
            {   
                'name': 'ratio',
                'min': queryset.order_by('lw')[0].lw,
                'max': queryset.order_by('-lw')[0].lw,
            },
            {   
                'name': 'sale_price',
                'min': queryset.order_by('sale_price')[0].sale_price,
                'max': queryset.order_by('-sale_price')[0].sale_price,
            },
            {   
                'name': 'table',
                'min': queryset.order_by('table_procent')[0].table_procent,
                'max': queryset.order_by('-table_procent')[0].table_procent,
            },
            {   
                'name': 'width',
                'min': queryset.order_by('width')[0].width,
                'max': queryset.order_by('-width')[0].width,
            },
        ]
        
        # <-- get max / min filter objects 
        max_min = MaxMin.objects.all()
        
        # --> update max / min values
        for value in values:
            for item in max_min:
                if item.name == value['name']:
                    item.min = value['min']
                    item.max = value['max']
                    item.save()

    # @ not auth
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('signin'))
    if request.user.user_type == '1':
        return redirect(reverse_lazy('client_info'))


    # ? this url
    this_url = 'white_diamonds'

    # ? get form
    form = UploadDiamondForm()

    # ? msg var
    msg = False

    # @ POST
    if request.method == 'POST':

        # * get file
        file = request.FILES['diamonds']
        
        # * check file type
        if not file.name.endswith('.csv'):
            messages.error(request, 'The uploaded file must be in the format: CSV')
            return redirect(reverse_lazy(this_url))

        # * get form
        form = UploadDiamondForm(request.POST)
        
        # * decode and read file
        file = request.FILES['diamonds'] 
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file, delimiter=";")

        # * read file + create diamond items
        diamonds = []
        for row in reader:
            # * get or create shape item
            try:
                shape = row['Shape'],
            except KeyError:
                messages.error(request, 'The submitted file is not a file with new stones')
                return redirect(reverse_lazy(this_url))
                
            # * get disc
            disc = round(float(row['Sale Price'].replace(',', '.')) / float(row['Weight'].replace(',', '.')) / float(row['Rap. price'].replace(',', '.')) , 1)
            disc = round(disc * 2, 2)

            # * get clarity num
            clarity_list = ['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FI']
            for index, value in enumerate(clarity_list):
                if value == row['Clarity']:
                    clarity_value = index

            # * get cut num
            cut_list = ['N/A','Fair','Good','Very Good','Ideal','Super Ideal','Excellent']
            for index, value in enumerate(cut_list):
                if value == row['Cut']:
                    cut_value = index

            # * get color num
            color_list = ['M','L','K','J','I','H','G','F','E','D']
            for index, value in enumerate(color_list):
                if value == row['Color']:
                    color_value = index

            # * get polish num
            polish_list = ['Good','Very Good','Excellent', 'N/A']
            for index, value in enumerate(polish_list):
                if value == row['Polish']:
                    polish_value = index

            # * get symmetry num
            symmetry_list = ['N/A','Good','Very Good','Excellent']
            for index, value in enumerate(symmetry_list):
                if value == row['Symmetry']:
                    symmetry_value = index

            # * get fluour num
            fluour_list = ['None','Faint','Medium','Strong','Very Strong']
            for index, value in enumerate(fluour_list):
                if value == row['Fluor. Note']:
                    fluour_value = index

            # * get shape num
            shape_list = ['Round', 'Marquise', 'Asscher', 'Cushion', 'Emerald', 'Heart', 'Oval', 'Pear', 'Princess', 'Radiant']
            shape_value = 10
            for index, value in enumerate(shape_list):
                if value == row['Shape']:
                    shape_value = index
                
            # * get lab num
            lab_list = ['IGI', 'GIA', 'GCAL', 'HDR']
            lab_value = 0
            for index, value in enumerate(lab_list):
                if value == row['Cert. Company']:
                    lab_value = index

            # --> create diamond
            diamond = {
                'ref': row['Ref'],
                'vendor': row['Vendor'],
                'vendor_id': row['Vendor ID'],
                'cert_number': row['Cert. Number'],

                'shape': shape_value,
                'shape_ex': row['Shape Ex'],
                
                'weight': row['Weight'].replace(',', '.'),
                'color': color_value,
                'color_comment': row['Color Comment'],
                'clarity': clarity_value,

                'rap_1ct': row['Rap. 1ct'].replace(',', '.'),
                'rap_price': row['Rap. price'].replace(',', '.'),
                'sale_price': round(float(row['Sale Price'].replace(',', '.')), 0),
                'disc': disc,

                'origin': row['Origin'],
                'cut': cut_value,
                'polish': polish_value,
                'symmetry': symmetry_value,

                # ?
                # 'gridle_from': row['Girdle From'],
                # 'gridle_to': row['Girdle To'],
                # 'gridle_type': row['Girdle Type'],
                # 'culet': row['Culet'],
                # 'fluorescence': row['Fluorescence'],
                # 'fluor': fluour_value,
                # ?

                'length': row['Length'].replace(',', '.'),
                'width': row['Width'].replace(',', '.'),
                'depth': row['Depth'].replace(',', '.'),
                'lw': round(float(row['Length'].replace(',', '.')) / float(row['Width'].replace(',', '.')), 2),

                'cert_company': lab_value,
                'depth_procent': row['Depth %'].replace(',', '.'),
                'table_procent': row['Table %'].replace(',', '.'),
                'warehouse': row['Warehouse'],
                'comments': row['Comments'],

                'photo': row['Image Link'],
                'video': row['Video Link'],
                
                'on_memo': row['On Memo'],
                'report_link': row['Report Link'],

                'key': f"{row['Ref']};{row['Vendor']};{row['Cert. Number']};{row['Color']};{row['Clarity']}",

            }

            # -->  create diamonds array
            diamonds.append(diamond)

        # * create action enumerate vaelu
        num_created = 0
        num_updated = 0

        # --> update or crete diamond in model
        for diamond in diamonds:
            
            # * create this key and this shape var
            key = diamond['key']

            stone, created = Diamond_Model.objects.update_or_create(key=key, defaults=diamond)

            if created:
                num_created += 1
            else:
                num_updated += 1

        # * get max / min values
        queryset = Diamond_Model.objects.all()
        update_max_min(queryset)


        # * success message
        msg = f"Created Stones: {num_created} | Updated Stones: {num_updated}"
        messages.success(request, 'The data was uploaded successfully')

    # * create context   
    context = {
        'title': 'Upload a whitelist',
        'form': form,
        'msg': msg
    }

    return render(request, 'upload_diamonds.html', context)
